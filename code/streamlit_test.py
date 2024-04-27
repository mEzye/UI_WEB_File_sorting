import streamlit as st
from functions import (
    deep_folders,
    rename_and_relocation,
    rename_and_relocation_without_arch,
    del_empty_dirs,
    result_sorting_with_arch,
    result_sorting_without_arch,
)

def main():
    st.title('Сортувалка')

    folder_path = st.text_input('Папка для сортування:')

    unpack_archives = st.checkbox('Розпаковка архівів')
    sort_nested_folders = st.checkbox('Сортувати у вкладених папках')

    st.warning('ПОПЕРЕДЖЕННЯ! Назви файлів з кириличними символами будуть транслітеровані!')

    if st.button('Сортувати!'):
        try:
            if unpack_archives and sort_nested_folders:
                deep_folders(folder_path)
                rename_and_relocation(folder_path)
                result_sorting_with_arch(folder_path)
            elif unpack_archives and not sort_nested_folders:
                rename_and_relocation(folder_path)
                result_sorting_with_arch(folder_path)
            elif not unpack_archives and sort_nested_folders:
                deep_folders(folder_path)
                rename_and_relocation_without_arch(folder_path)
                result_sorting_without_arch(folder_path)
            else:
                rename_and_relocation_without_arch(folder_path)
                del_empty_dirs(folder_path)
                result_sorting_without_arch(folder_path)
            st.success(f'Сортування виконано для папки: {folder_path}')
        except Exception as e:
            st.error(f'Помилка: {str(e)}')

if __name__ == '__main__':
    main()