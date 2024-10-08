class Locators:
    # Регистрация
    registration_name = './/label[ text()="Имя" ]/parent::div/input'  # поле Имя на странице регистрации
    registration_email = './/label[ text()="Email" ]/parent::div/input'  # поле Email на странице регистрации
    registration_password = './/label[ text()="Пароль" ]/parent::div/input'  # поле Пароль на странице регистрации
    registration_button = './/button[ text()="Зарегистрироваться" ]'  # кнопка Зарегистрироваться на странице регистра
    registration_invalid_password = './/p[ text()="Некорректный пароль" ]' # Уведомление о неправильном пароле

    #Авторизация
    autorization_personal_cabinet_button = './/header/nav/a' #Кнопка "личный кабинет" на главной
    autorization_enter_in_account_button = ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']//button" #Кнопка
    # "Войти в аккаунт" на главной
    enter_on_registration_page = ".//a[@class='Auth_link__1fOlj']" #Ссылка "Войти" на странице регистрации
    text_on_main_page = ".//h1[@class='text text_type_main-large mb-5 mt-10']" #Текст на главной "Соберите бургер"
    text_in_cabinet = ".//p[text()='В этом разделе вы можете изменить свои персональные данные']" #Текст для проверки отображения лк
    button_logout = ".//button[text()='Выход']" #Кнопка выхода из лк
    text_in_log_in = ".//h2" #Текст "Вход" на странице входа
    header_logo = ".//div/a" #Лого сайта в хедере
    header_constructor = ".//a" # Кнопка "Конструктор" в хедере
    enter_link_registration = ".//a[text()='Зарегистрироваться']" #Ссылка Зарегистрироваться на странице входа
    enter_forgot_password = ".//a[text()='Восстановить пароль']" #Ссылка "Восстановить паоль" на стрранице входа


    autorization_email = ".//input[@name='name']" #Поле для ввода емайл на странице входа
    autorization_password = ".//input[@name='Пароль']" #Поле для ввода пароля на странице входа
    autorization_button = './/button' #Кнопка "Войти" на странице входа

    #Разделы конструктора
    constructor_section_breads = ".//span[text()='Булки']/parent::div" # Раздел "Булки" в констуркторе
    constructor_section_sauce = ".//span[text()='Соусы']/parent::div" # Раздел "Соус" в констуркторе
    constructor_section_filling = ".//span[text()='Начинки']/parent::div"  # Раздел "Начинка" в констуркторе
