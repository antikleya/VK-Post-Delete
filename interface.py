from vkpostdeleter import VkPostDeleter
import PySimpleGUI as sg
import vk_api


def display_error(error_text: str):
    sg.popup(error_text, title='Error')


def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Login'), sg.InputText(key='login')],
                [sg.Text('Password'), sg.InputText(password_char='*', key='password')],
                [sg.Text('Offset'), sg.InputText(key='offset')],
                [sg.Button('Connect'), sg.Button('Delete'), sg.Button('Cancel')]]

    # Create the Window and VkPostDeleter instance
    window = sg.Window('Vk post deleter', layout)
    vk = VkPostDeleter()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # close event handler
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        # delete event handler
        elif event == 'Delete':
            # input error handlers

            # login check
            if not vk.logged_in:
                display_error("You need to login first. Enter your login and password and press 'Connect'")
            else:
                # invalid offset check
                try:
                    offset = int(values['offset'])
                except ValueError:
                    display_error(values['offset'] + ' is not a valid number')
                else:
                    # negative offset check
                    if offset < 0:
                        display_error('offset should be positive')
                    # no input errors case
                    else:
                        vk.delete_with_offset(values['offset'])

        # Connect event handler
        elif event == 'Connect':
            # input error handlers

            # empty login check
            if values['login'] == '':
                display_error('login is empty')
            # empty password check
            elif values['password'] == '':
                display_error('password is empty')

            # no input errors case
            else:
                try:
                    vk.login(values['login'], values['password'])
                except vk_api.exceptions.BadPassword:
                    display_error('Wrong login or password')

    window.close()


if __name__ == '__main__':
    main()
