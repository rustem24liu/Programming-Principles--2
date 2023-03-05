import easygui
flavor = easygui.enterbox('Ваше любимое мороженное?',
                          default = 'Ванильное')
easygui.msgbox('Вы указали ' + flavor)