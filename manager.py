from application import app


def main():
    app.run(debug=True)


if __name__ == '__main__':
    try:
        import sys
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
