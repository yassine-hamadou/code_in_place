from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def main():
    user_text = input("Text: ")
    score = get_sentiment(user_text)
    reaction = get_reaction(score)
    print(reaction)
    print(score)
    print('')


def get_reaction(score):
    if score > 0.5:
        return "😀"
    if score > 0:
        return "🙂"
    if score == 0:
        return "😐"
    if score > -0.5:
        return "😟"
    if score < 0:
        return "😔"


def get_sentiment(user_text):
    dicti = analyzer.polarity_scores(user_text)
    score = dicti['compound']
    return score


if __name__ == '__main__':
    main()