const langArr = {
    "instruction":{
        "ru": "Инструкция",
        "en": "Instructions"
    },

    "Tab":{
        "ru": "Вы можете озакномиться с содержимым таблиц ниже:",
        "en": "You can read the observation records in the following tables:"
    },

    "tab1":{
        "ru": "Прежде чем перейти к заданию, давайте рассмотрим демонстрационный материал.",
        "en": "Before we move on to the task itself, let's look at the demonstration material."
    },

    "tab2":{
        "ru": "Перед вами две таблицы с наблюдениями. И для простоты в них выписаны наблюдения только для X и Y. Таблица справа, это таблица для планеты-близнеца (все зёрна переменной X зрелые).",
        "en": "Here we have two tables with observations. For simplicity, only the observations for X and Y are written out in them. The table on the right is the table for the twin planet (all grains of variable X are mature)."
    },

    "tab3":{
        "ru": "В данном демонстрационном материале, для того чтобы вам было легче познакомиться с задачей сделаны два упрощения. Все зрелые зерна выделены цветом. Все клумбы находятся не над каменистыми почвами. ",
        "en": "In this demo, to make it easier for you to familiarize yourself with the problem, two simplifications are made. All mature grains are highlighted in color. All beds are not over rocky soils. "
    },

    "tab4":{
        "ru": "Пожалуйста заполните форму ответа, в соответствии с вашими предположениями о том, какие зависимости между сильными и слабыми растениями следуют из данных таблиц.",
        "en": "Please fill in the answer form according to your assumptions about what relationships between strong and weak plants follow from these tables."
    },

    "tab12":{
        "ru": "Это последний демо-материал перед переходом к заданию. В нем представлены точно такие-же наблюдения какие демонстрировались прошлый раз, с двумя отличиями.",
        "en": "This is the last demo material before moving on to the task. It presents exactly the same observations as the last demo, with two differences."
    },

    "tab22":{
        "ru": "Первое: зрелые семена так же расположены по тем же номерам клумб, но больше нет выделения цветом. Второе: клумба №1 в таблице слева и клумба №3 в таблице справа теперь находятся на каменистых почвах. Обратите внимание, что хоть номера клумб и не совпадают, количество зрелых семян распределённое по каменистым клумбам всегда одинаковое на обоих планетах.",
        "en": "First, the mature seeds are still arranged by the same bed numbers, but there is no more color selection. Second, bed 1 in the table on the left and bed 3 in the table on the right are now on rocky soils. Note that although the bed numbers are not the same, the number of mature seeds distributed on the rocky beds is always the same on both planets."
    },

    "carSlide1String1":{
        "ru": "Ваша сессия состоит из "+js_vars.num_rounds+" раундов.  В каждом раунде Вам предстоит выполнять типовые задания, цель и структура которых, не меняется от раунда к раунду.",
        "en": "The session consists of "+js_vars.num_rounds+" rounds. In each round you will be asked to perform identical tasks that do not differ in structure or purpose."
    },

    "carSlide1String2":{
        "ru": `Внутри каждого задания вам предстоит ознакомиться с наборами данных, которые разбиты по столбцам (всего 3 столбца). Каждый столбец содержит 16 строк.
               Значение строки в каждом столбце может принимать значения 0 и 1.
               Каждое такое значение является результатом <i>случайного</i> выбора системы,
               однако частота их генерации определяется механизмом, закрепленным за каждым столбцом.`,

        "en": `Inside each assignment you will be given sets of data, which are divided into columns (3 columns in total). Each column contains 16 rows.
               The value of a row in each column can take the values 0 and 1.
               Each such value is the result of a <i>random</i> choice of the system,
               but the frequency of their occurence depends on mechanism assigned to each column.`
    },

    "carSlide1String3":{
        "ru": `<b>Частота генерации</b> внутри столбца может зависеть от механизма в другом столбце.
               Это будет означать что если такая зависимость в задании в раунде есть, то значения в столбцах будут генерироваться последовательно, сначала в одном столбце, потом в зависимом от него.`,

        "en": `If the columns are dependent, then in one of them certain values have been randomly selected, and in the other one the <b>generation frequency</b> on the corresponding rows has changed.
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
              значения в одном из столбцов (Вы будете знать в каком) будут заменены единицами в первую очередь, а после будут определены значения в остальных столбцах.
              Такая операция будет называться DO (название столбца) и для этого будет отдельная кнопка над столбцом.`,

        "en": `In each task you will have the opportunity to start the generation process again as follows:
              the values in one of the columns (you will always know which one) will be changed to ones first, and then the values in the other columns will be determined.
              This operation will be called DO (column name) and there will be a separate button above column.`
    },

    "carSlide3String1":{
        "ru": `Один из элементов управления таблицей позволит Вам отображать только те значения, 
        которые принимает один конкретный столбец, однако это будут те же значения, которые были сгенерированы системой 
        изначально и изменятся будет только их отображение на экране в таблице. Такая операция будет доступна для каждого столбца. 
        Чтобы её совершить нужно будет выставить галочку напротив значения 0 или 1 под названием столбца.
        `,

        "en": `One of the table controls (filter) will allow you to display only the values that one particular column takes.
              But these will be the same values that were originally generated by the system and only their display in the table will change.
              This operation will be available for each column. To do this, you will need to check the box next to the value 0 or 1 under the column name.`
    },

    "carSlide3String2":{
        "ru": `Задача каждого раунда — определить, зависит ли частота генерации каждого столбца от механизмов генерации в других столбцах.`,

        "en": `The task of each round is to determine whether the frequency of generation of each column depends on the mechanisms in the other columns.`
    },

    "carSlide3String3":{
        "ru": `В задании последовательность генерации <b>не может</b> быть длиннее трех шагов, т.е. между столбцами не может быть циклов зависимости.
              Это исключает ситуации, в которых, например, столбец X зависит от Y, Y зависит от Z, а Z зависит от X или когда X зависит от Y, а Y зависит от X.`,

        "en": `In this task, the generation sequence <b>cannot be</b> longer than three steps, i.e. there cannot be dependency cycles between columns.
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
        "ru": `Вы можете ознакомиться с записями наблюдений в следующих таблицах:`,

        "en": `You can read the observation records in the following tables:`
    },

    "TrText":{
        "ru": `Давайте разберемся, как заполнять форму!
               Выберите (нажмите) стрелки следующим образом: оставьте ребро пунктирным, если одна переменная не влияет на другую переменную, и сделайте его сплошным, если влияет.
               В качестве примера заполните форму для следующей ситуации: столбец Y зависит от X. После этого нажмите Next.`,

        "en": `Lets figure out how to fill the form!
        Choose (click) the arrows as follows: leave the edge dashed if there is no influence from one variable to another variable and make it solid if there is.
        As an example please fill the form for following situation: column Y are dependent from X. Then tap Next.`
    },

    "DtText":{
        "ru": `Пожалуйста, заполните следующую форму, если считаете что между некоторыми из переменных X, Y и Z есть связь. `,

        "en": `Please, fill out the form if you assume any relationships between X, Y and Z`
    },

    "confidence":{
        "ru": `Выберите уровень своей уверенности`,

        "en": `Choose your confidence`
    },

    "DTestTitle":{
        "ru": `Решения в последнем раунде:`,

        "en": `You accuracy in last round:`
    },

    "DTestText1":{
        "ru": `То, что было выбрано:`,

        "en": `That what was chosen:`
    },

    "DTestText2":{
        "ru": `Те зависимости, на основе которых были сгенерированы данные:`,

        "en": `These dependencies are underlying the basis of the data:`
    },

    "confstart":{
        "ru": `Используя бегунок укажите, насколько вы уверены в своем ответе`,

        "en": `Please choose how confident you are using slider`
    },
    "conflevel":{
        "ru": `Текущее значение:`,

        "en": `Current confidience:`
    },
    "Accuracy":{
        "ru": `Ваша точность за этот раунд:`,

        "en": `Your accuracy for the round is`
    },
    "Meanaccuracy":{
        "ru": `Ваша средняя точность за все раунды:`,

        "en": `Your mean accuracy for the rounds is`
    },
    "Totalscore":{
        "ru": `Сумма выигрыша составила:`,

        "en": `Your total payoff`
    },
}
