import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression pattern to find the YouTube URL
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/(\w+)"[^>]*>'

    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        head_link = "https://youtu.be/"
        return f"{head_link}{video_id}"

    return None

if __name__ == "__main__":
    main()