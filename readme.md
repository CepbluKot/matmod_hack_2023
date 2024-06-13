# Проект "Система контроля состояния двигателя".
## О проекте
Наша команда реализует услугу по замене части стороннего ПО в S7. В будущем это позволит авиакомпании расширить сферу влияния.

Ранее использовался зарубежный софт, но после введия санкций в виду того, что большинство этих сервисов были облачными, их поддержка на территории России либо ограничена, либо полностью прекращена. Формулы, по которым авиакомпания рассчитывала показатели, важные для технического обслуживания, не раскрываются поставщиком ПО. На основании этих показателей рассчитываются оценки износа двигателя и строится график для аналитического анализа.

Наша задача - на основе данных с датчиков двигателей и ранее полученных данных из специализированного ПО разработать модели машинного обучения для расчёта параметров, важных для технического обслуживания. Полученные модели позволят заменить иностранное ПО.

## Итог

Команда заняла 2-е место

## Задачи
* Получить и обработать входные параметры формата *.csv
* Предсказать performance значения для каждого полетного цикла.
* Определить зависимости между выходными параметрами
* Разработать серверную часть приложения и удобный пользовательский интерфейс.

## Решение
Загружаются выборки параметров с датчиков и реальные значения для ТО. На основе выбранных моделей самолета и двигателя на модуль машинного обучения отправляются данные с датчиков для расчёта нужных параметров. Вместе с фактическими значениями они отправляеются на пользовательский интерфейс, где выбирается один из доступных параметров и происходит построение графика зависимостей его от времени.

## Развёртывание приложения

docker compose up

## Ссылки
Презентация решения - https://github.com/CepbluKot/matmod_hack_2023/blob/master/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0%20NAGOOR%20BABY.pptx

Материалы - https://drive.google.com/drive/folders/1PyXlq-zqpFHwc6dpXPTzoS6wRbSn5-ib?usp=sharing

Репо с бекендом - https://gitlab.com/Velovatik1/s7-ecm-backend

Репо с бекендом для ML - https://gitlab.com/CepbluKot/matmod_challenge_ml_back

Репо с исследованием ML - https://gitlab.com/CepbluKot/matmod_challenge

Репо с фронтендом - https://gitlab.com/rodinf/s7-ecm-frontend


## Команда
[Дмитрий Краснов - бекенд](http://t.me/Dm1ttry) </br>
[Игорь Малыш - МЛ + бекенд для МЛ](http://t.me/igmalysh) </br>
[Федор Родин - фронтенд](http://t.me/ffeeejj) </br>
[Веловатый Кирилл - бекенд](http://t.me/velovatik) </br>

## Диплом
![](https://github.com/CepbluKot/matmod_hack_2023/blob/master/diplom.jpg)
