pip install youtube-comment-downloader
from youtube_comment_downloader import YoutubeCommentDownloader

downloader = YoutubeCommentDownloader()
VIDEO_ID = "DDpmHTskfZ8"  # Replace with your actual video ID

# Convert generator to a list
comments = list(downloader.get_comments(VIDEO_ID))

# Display first 10 comments
for idx, comment in enumerate(comments[:1000]):  
    print(comment['text'])
