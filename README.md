[![Typing SVG](https://readme-typing-svg.herokuapp.com?size=30&color=081D26&lines=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82!)](https://git.io/typing-svg)
<p>Этот проект представляет из себя сайт, позволяющий добавлять игры из других источников, использовать чат и, в случае неполадок, дающий пользователям поддерживать связь с тех. поддержкой.</p>

<p>Для того,  чтобы запустить наш проект у себя тебе нужно выполнить несколько шагов:</p>

<p>1) скачать и установить docker (инструкции для 
<a href="https://docs.docker.com/desktop/windows/install/">windows</a>, 
<a href="https://docs.docker.com/desktop/linux/install/">linux</a> и 
 <a href="https://docs.docker.com/desktop/mac/install/">mac</a>).<br><b>В случае windows для того, чтобы контейнер запустился, нужно чтобы было запущена только что установленная программа docker.</b></p>

<p>2) установить git (<a href="https://github.com/git-guides/install-git#:~:text=To%20install%20Git%2C%20navigate%20to,installation%20by%20typing%3A%20git%20version%20.">инстукция</a>) и склонировать наш проект (выполнить команду в термиале "git clone --recursive https://github.com/pashatehnik/upprpo.git") или скачать zip файлом.</p>

<p>3) затем в терминале перейти в корень проекта и выполнить последовательно команды:</p>
<p style="margin-left: 40px">docker-compose build
<br>
  <br>
docker-compose up
</p>
<p>
если все запустилось, останавливаем контейнер и вызываем:
</p>
<p style="margin-left: 40px"> docker-compose run app sh -c "python manage.py createsuperuser"
 </p>
<p>придумываем и вводим username, password, email для суперпользователя.</p>
<p> далее снова запускаем контейнер (docker-compose up),</p>
переходим по адресу <a href="https://localhost:8000/">https://localhost:8000/</a> и получаем запущенный сайт. <br>
Для администрирование переходим по адрессу <a href="https://localhost:8000/admin">https://localhost:8000/admin</a> и вводим логин и пароль суперпользователя.

<br>
<p>Если нужно удалить созданный ранее контейнер - <b>docker-compose down</b>, для остановки контейнера <b>Ctrl+C</b>.</p>


