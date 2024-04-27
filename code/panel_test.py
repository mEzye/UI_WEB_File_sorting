import panel as pn
import tkinter as tk
from tkinter import filedialog
from functions import (
    deep_folders, rename_and_relocation, rename_and_relocation_without_arch,
    del_empty_dirs, result_sorting_with_arch, result_sorting_without_arch,
)

pn.extension('tkhtmlwidgets')

def callback():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def main():
    address = pn.widgets.TextInput(name='Папка для сортування:')
    select_folder = pn.widgets.Button(name='Вибрати папку', button_type='primary')
    unpack_var = pn.widgets.Checkbox(name='Розпаковка архівів')
    deep_var = pn.widgets.Checkbox(name='Сортувати у вкладених папках')
    sort_button = pn.widgets.Button(name='Сортувати!', button_type='success')
    warning = pn.pane.Alert("ПОПЕРЕДЖЕННЯ! Назви файлів з кириличними символами будуть транслітеровані!", alert_type='warning')

    def on_select_folder_click(event):
        address.value = callback()

    select_folder.on_click(on_select_folder_click)

    def on_sort_click(event):
        try:
            if unpack_var.value and deep_var.value:
                deep_folders(address.value)
                rename_and_relocation(address.value)
                result_sorting_with_arch(address.value)
            elif unpack_var.value and not deep_var.value:
                rename_and_relocation(address.value)
                result_sorting_with_arch(address.value)
            elif not unpack_var.value and deep_var.value:
                deep_folders(address.value)
                rename_and_relocation_without_arch(address.value)
                result_sorting_without_arch(address.value)
            else:
                rename_and_relocation_without_arch(address.value)
                del_empty_dirs(address.value)
                result_sorting_without_arch(address.value)
        except Exception as e:
            pn.pane.Alert(f"Помилка: {str(e)}", alert_type='danger')

    sort_button.on_click(on_sort_click)

    app = pn.Column(
        address,
        select_folder,
        unpack_var,
        deep_var,
        sort_button,
        warning,
    )

    return app

pn.serve(main)