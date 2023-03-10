const langArr = {
    "instruction":{
        "ru": "Инструкция",
        "en": "Instructions"
    },

    "carSlide1String1":{
        "ru": "Ваша сессия состоит из "+js_vars.num_rounds+" раундов.  В каждом раунде Вас будут просить выполнять типовые задания, не отличающиеся по своей структуре и цели выполнения.",
        "en": "The session consists of "+js_vars.num_rounds+" rounds. In each round you will be asked to perform identical tasks that do not differ in structure or purpose."
    },

    "carSlide1String2":{
        "ru": `Внутри каждого задания вам предстоит ознакомиться с наборами данных, которые разбиты по столбцам (всего 3 столбца). Каждый столбец содержит 16 строк.
              Значение строки в каждом столбце может принимать значения 0 и 1.
              Каждое такое значение является результатом случайного выбора системы,
              однако частота их генерации определяется механизмом, закрепленным за каждым столбцом.`,

        "en": `Inside each assignment you will be given sets of data, which are divided into columns (3 columns in total). Each column contains 16 rows.
              The value of a row in each column can take the values 0 and 1.
              Each such value is the result of a random choice of the system,
              but the frequency of their occurence depends on mechanism assigned to each column.`
    },

    "carSlide1String3":{
        "ru": `Если столбцы зависимы, то в одном из них случайном образом были выбраны определённые значения, а в другом частота генерации на соответствующих строках изменилась.
              Например, если Y зависит от X, то может произойти так, что в столбце Y единица будет генерироваться чаще (или реже) на тех строках, которые в столбце X также были единицами.`,

        "en": `If the columns are dependent, then in one of them certain values have been randomly selected, and in the other one the generation frequency on the corresponding rows has changed.
              For example, if Y is dependent on X, it may happen that column Y generates a one more often (or less often) on those rows that were also ones in column X.`
    },

    "carSlide2String1":{
        "ru": `Однако в каждом раунде вам не будет известно есть ли зависимость между столбцами, и в какой последовательности они были сгенерированы (если зависимостей нет, то это не имеет значения).
              Вы будете наблюдать только наборы данных (таблицу с тремя столбцами X, Y и Z) сформированные после того, как система запустит работу механизмов.`,

        "en": `However, in each round, you will not know if there is a dependency between columns, and in what sequence they were generated (if there is no dependency, then it does not matter).
              You will only observe data sets (a table with three columns X, Y and Z) generated after the system runs the mechanisms.`
    },

    "carSlide2String2":{
        "ru": `В каждом задании Вы можете перезапустить процесс генерации следующим образом:
              значения в одном из столбцов (Вы будете знать в каком) будут заменены единицами, а значения в других столбцах будут соответственно переопределены.
              Обозначим такое действие за &quot;DO &lt;column name&gt;&quot;, для него будет отдельная кнопка.`,

        "en": `In each task you will have the opportunity to start the generation process again as follows:
              the values in one of the columns (you will always know which one) will be changed to ones first, and then the values in the other columns will be determined.
              This operation will be called &quot;DO &lt;column name&gt;&quot; and there will be a separate blue button for it.`
    },

    "carSlide3String1":{
        "ru": `Один из элементов таблицы (фильтрация) позволит вам отображать лишь те значения, которые принимает конкретный столбец.
              Но это будут те же значения, которые изначально были сгенерированы системой, изменится только их отображение в таблице
              Такая операция доступна для каждого столбца. Чтобы ее запустить, Вам нужно поставить галочку возле 0 или 1 под названием столбца`,

        "en": `One of the table controls (filter) will allow you to display only the values that one particular column takes.
              But these will be the same values that were originally generated by the system and only their display in the table will change.
              This operation will be available for each column. To do this, you will need to check the box next to the value 0 or 1 under the column name.`
    },

    "carSlide3String2":{
        "ru": `Задача каждого раунда — определить, зависит ли частота генерации каждого столбца от механизмов генерации в других столбцах.`,

        "en": `The task of each round is to determine whether the frequency of generation of each column depends on the mechanisms in the other columns.`
    },

    "carSlide3String3":{
        "ru": `В этой задаче последовательность генерации не может быть длиннее трех шагов, т.е. между столбцами не может быть циклов зависимости.
              Это исключает ситуации, в которых, например, столбец X зависит от Y, Y зависит от Z, а Z зависит от X или когда X зависит от Y, а Y зависит от X.`,

        "en": `In this task, the generation sequence cannot be longer than three steps, i.e. there cannot be dependency cycles between columns.
              This eliminates situations where, for example, column X is dependent on Y, Y is dependent on Z and Z is dependent on X, or where X is dependent on Y and Y is dependent on X.`
    },

    "carSlide4String1":{
        "ru": `Из предыдущего абзаца следует, что одновременно может быть верным только одно из следующих утверждений:
              каждый механизм генерации столбцов может либо влиять на другой, либо зависеть от него, либо два механизма не влияют друг на друга.`,

        "en": `It follows from the previous paragraph that only one of the following statements can be true at a time:
              each column generation mechanism can either influence or be dependent on the other one, or two mechanisms do not influence each other.`
    },

    "carSlide4String2":{
        "ru": `Частоты в каждом столбце в этом задании будут сформированы таким образом, что не будет иметь значения, предоставлено ли для их анализа 16 строк или 16 000 строк,
              все закономерности сохраняются.`,

        "en": `The frequencies in each column in this assignment will be generated in such a way that it does not matter whether 16 rows or 16,000 rows are provided for their analysis,
              all patterns will hold.`
    },

    "carSlide4String3":{
        "ru": `Ваш ответ в каждом раунде необходимо будет ввести в графическую форму. В ней каждое имя столбца будет иметь две входящие и две исходящие стрелки (ребра).
              Если Вы считаете, что один из столбцов зависит от другого, Вам нужно будет нажать на стрелку, чтобы сделать ее активной, после чего пунктирная линия превратится в сплошную.`,

        "en": `Your answer in each round, will need to be entered into a graphical form. In it, each column name will have two incoming and two outgoing arrows (edges).
              If you think one of the columns depends on the other, you will need to click on the arrow to make it active, then the dotted line will change to a solid line.`
    },

    "IReadTheSlides":{
        "ru": `С помощью стрелочек < >, Я внимательно прочитал все слайды и понимаю задание.`,

        "en": `Using < > elements, I carefully read all slides and understand the task.`
    },

    "Title":{
        "ru": `Выберите соответствующие стрелки (ребра) между переменными согласно данным.`,

        "en": `Pick the arrows (edges) between variables according to data.`
    },

    "TrText":{
        "ru": `Давайте разберемся, как заполнять форму!
               Выберите (нажмите) стрелки следующим образом: оставьте ребро пунктирным, если одна переменная не влияет на другую переменную, и сделайте его сплошным, если есть.
               В качестве примера заполните форму для следующей ситуации: столбец Y зависит от X. После этого нажмите Next.`,

        "en": `Lets figure out how to fill the form!
        Choose (click) the arrows as follows: leave the edge dashed if there is no influence from one variable to another variable and make it solid if there is.
        As an example please fill the form for following situation: column Y are dependent from X. Then tap Next.`
    },

    "DtText":{
        "ru": `Выберите (нажмите) ребра следующим образом: оставьте ее пунктирной, если одна переменная не влияет на другую переменную, или сделайте е сплошной, если есть.
            Помните, что каждая переменная может быть ЛИШЬ ОДНИМ из следующих вариантов: а) независимой б) причиной в) следствием.`,

        "en": `Choose (click) the edges as follows: leave it dashed if there is no influence from one variable to another variable, or make it solid if there is.
            Remember that each variable could be simultaneously ONLY ONE of the following: a) independent b) cause с) effect.`
    },

    "confidence":{
        "ru": `Выберите уровень своей уверенности`,

        "en": `Choose your confidence`
    },

    "DTestTitle":{
        "ru": `Выберите ребра и узлы.`,

        "en": `Pick the edges and nodes.`
    },

    "DTestText1":{
        "ru": `Вы расставили следующие связи`,

        "en": `That what was chosen`
    },

    "DTestText2":{
        "ru": `Настоящие зависимости выглядят следующим образом (Процесс Генерации Данных)`,

        "en": `That is the original dependencies (Data Generation Process)`
    },

}