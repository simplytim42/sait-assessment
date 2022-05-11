from wordcloud import WordCloud

def generate_wordcloud(filepath):
    wordcloud_filename = 'static/wordcloud.png'

    with open(filepath) as file:
        data = file.read()

    wordcloud = WordCloud(height=400, width=600).generate(data)
    wordcloud.to_file(wordcloud_filename)