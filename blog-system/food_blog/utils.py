def calculate_reading_time(text):
    words_per_minute = 150  # Average reading speed
    word_count = len(text.split())
    reading_time = round(word_count / words_per_minute)
    return reading_time  # Ensure a minimum of 1 minute