import googleapiclient
import argparse
from google.cloud import language_v1
import six
import os
from google.cloud import language
from google.oauth2 import service_account


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/kingjung/Documents/Google Cloud Vertex AI Hackathon/participant-sa-2-ghc-023.json"



def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(f"Sentence {index} has a sentiment score of {sentence_sentiment}")

    print(f"Overall Sentiment: score of {score} with magnitude of {magnitude}")
    return 0




def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    with open(movie_review_filename) as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    annotations = client.analyze_sentiment(request={"document": document})

    # Print the results
    print_result(annotations)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.movie_review_filename)

def sample_analyze_sentiment(content):
    creds = service_account.Credentials.from_service_account_file('participant-sa-2-ghc-023.json')
    client = language_v1.LanguageServiceClient(credentials=creds)

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))
    

c1 = "Tesla is a joke"
sample_analyze_sentiment(c1)