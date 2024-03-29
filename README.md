# backend_community_homework

## Спринт 4.
Расширение учебного проекта **Yatube** на фреймворке **Django**.  
Социальная сеть с возможностью создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи.

### В рамках расширения проекта:
- Настроен эмулятор отправки писем; отправленные письма должны сохраняться в виде текстовых файлов в директорию */sent_emails*. Настроена отправка письма при восстановлении пароля. 
- Создано и подключено приложение ***core***. В нём:
    - размещён и зарегистрирован фильтр `addclass`, позволяющий добавлять ***CSS***-класс к тегу шаблона
    - создан и зарегистрирован контекст-процессор, добавляющий текущий год на все страницы в переменную `{{ year }}`
- Создано и подключено приложение `about`, в нём:
    - созданы статические страницы ***/about/author/*** и ***/about/tech/***
    - ссылки на эти страницы добавлены в навигацию сайта
- Для всех путей установлены `name` и `namespace`
- Подключено приложение **django.contrib.auth**, его `urls.py` подключен к головному `urls.py`
- Создано и подключено приложение users, в нём:
    - Переопределены шаблоны для адресов
      - `/auth/login/` (авторизация),
      - `/auth/logout/` (выход из аккаунта).
    - Создана страница `/auth/signup/` с формой для регистрации пользователей
В приложении `posts`:
  - Создана страница пользователя `profile/<username>/`. На ней отображаются посты пользователя.
  - Создана отдельная страница поста `posts/<post_id>/`.
  - Подключен паджинатор, он выводит по десять постов:
    - на главную страницу,
    - на страницу профайла,
    - на страницу группы.
- Создана навигация по разделам.
- Сделана форма для публикации новых записей:
    - Добавлена в шапку сайта ссылка «Новая запись», она видна только авторизованным пользователям и ведет на страницу `/create/`
    - На странице `/create/` создана форма для добавления новой публикации:
        * **view**-функция для страницы `/create/` называется `post_create()`;
        * `name` для `path()` страницы `/create/` должен быть `post_create`;
        * в контекст шаблона страницы `/create/` передавается переменная `form`. Она содержить объект **PostForm**, в котором два поля:
            - `text` (обязательное для заполнения поле);
            - `group` (необязательное для заполнения);
            - после валидации формы и создания нового поста автор перенаправляется на страницу своего профайла `/profile/<username>/`
- Добавлена страница редактирования записи с адресом */posts/<post_id>/edit/*. **View**-функция для этой страницы называется `post_edit()`.
  - Права на редактирование есть только у автора этого поста. Остальные пользователи перенаправляются на страницу просмотра поста.
  - При генерации страницы в контекст передается переменная `form`, в ней два поля: `text` и `group`
  - Для страницы редактирования поста применяется тот же **HTML**-шаблон, что и для страницы создания нового поста: *posts/create_post.html*, для этого:
      - при редактировании поста заголовок **«Добавить запись»** заменяется на **«Редактировать запись»**;
      - надпись на кнопке отправки формы также зависит от операции: **«Добавить»** для новой записи и **«Сохранить»** — для редактирования.

#### Стек технологий: Python, Django, HTML, CSS
