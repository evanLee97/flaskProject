from application import app
import www


def main():
    app.run(host='0.0.0.0',
            port=49999,
            debug=True)


if __name__ == '__main__':
    try:
        import sys
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
