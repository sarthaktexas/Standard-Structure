from pyfiglet import Figlet

def main():
    
    custom_fig = Figlet(font = "banner3")

    ascii_banner = custom_fig.renderText("Hello World")

    print(ascii_banner)


if __name__ == "__main__":

    main()