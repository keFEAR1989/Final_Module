# README

## Описание тестов

Этот репозиторий содержит автотесты для проверки функциональности системы авторизации и управления аккаунтом веб-приложения "Умный дом". Ниже перечислены сценарии, которые проверяются с помощью этих автотестов:

1. **Авторизация с корректными данными (по номеру телефона и почте):** Тесты проверяют успешную авторизацию пользователей с правильными номерами телефонов и электронными адресами.

2. **Некорректный ввод номера телефона и электронной почты:** Тесты проверяют обработку ошибок при вводе некорректных данных.

3. **Блокировка аккаунта после нескольких неверных попыток ввода кода:** Тесты проверяют, что аккаунт блокируется после определенного числа неверных попыток ввода кода.

4. **Изменение номера телефона и электронной почты:** Тесты проверяют возможность смены номера телефона и электронной почты после успешной авторизации.

5. **Повторная отправка кода после истечения времени:** Тесты проверяют, что система позволяет пользователю запросить новый код после истечения времени действия предыдущего.

6. **Смена пароля после успешной авторизации:** Тесты проверяют возможность смены пароля после успешной авторизации.

7. **Смена пароля с недостаточно сильным паролем:** Тесты проверяют, что система требует ввода достаточно сильного пароля при его смене.

8. **Выход из аккаунта:** Тесты проверяют корректное завершение сеанса пользователя и выход из аккаунта.

9. **Отрицательная авторизация с недействительным кодом:** Тесты проверяют, что пользователь не может авторизоваться с недействительным кодом.

10. **Отрицательная авторизация с неверными учетными данными:** Тесты проверяют, что пользователь не может авторизоваться с неверными номерами телефона и электронными адресами.

11. **Сброс пароля и восстановление доступа:** Тесты проверяют процесс сброса пароля и восстановления доступа к аккаунту.

## Запуск тестов

Для запуска автотестов на вашем компьютере, убедитесь, что у вас установлен Python3 и библиотека PyTest. Если их нет, вы можете установить их следующим образом:

# Установка Python3 (если не установлен)
sudo apt-get install python3

# Установка pip3 (если не установлен)
sudo apt-get install python3-pip

# Установка библиотеки PyTest
pip3 install pytest
