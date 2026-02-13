import sys
from src.mashup import create_mashup


def main():

    try:

        # Check parameter count
        if len(sys.argv) != 5:

            print("Usage:")
            print("python 102303599.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
            return

        singer = sys.argv[1]

        try:
            count = int(sys.argv[2])
            duration = int(sys.argv[3])
        except ValueError:

            print("Error: NumberOfVideos and AudioDuration must be integers")
            return

        output = sys.argv[4]

        # Validate inputs
        if count <= 10:

            print("Error: NumberOfVideos must be greater than 10")
            return

        if duration <= 20:

            print("Error: AudioDuration must be greater than 20 seconds")
            return

        print("Starting Mashup Creation...")
        print(f"Singer: {singer}")
        print(f"Videos: {count}")
        print(f"Duration: {duration}")

        result = create_mashup(
            singer,
            count,
            duration,
            output
        )

        print("\nMashup created successfully")
        print("Output file location:", result)

    except Exception as e:

        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
