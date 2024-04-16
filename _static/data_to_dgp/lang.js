const langArr = {
    "instruction":{
        "ru": "Инструкция",
        "en": "Instructions",
        "ge": "Anweisungen",
    },

    "Tab":{
        "ru": "Вы можете озакномиться с содержимым таблиц ниже:",
        "en": "You can read the observation records in the following tables:",
        "ge": "Die Beobachtungssätze können Sie in den folgenden Tabellen nachlesen:",
    },

    "tab1":{
        "ru": "Прежде чем перейти к заданию, давайте рассмотрим демонстрационный материал.",
        "en": "Before we move on to the task itself, let's look at the demonstration material.",
        "ge": "Bevor wir uns der eigentlichen Aufgabe zuwenden, wollen wir uns das Anschauungsmaterial ansehen.",
    },

    "tab2":{
        "ru": "Перед вами две таблицы с наблюдениями. И для простоты в них выписаны наблюдения только для X и Y. Таблица справа, это таблица для планеты-близнеца (все зёрна переменной X зрелые).",
        "en": "Here we have two tables with observations. For simplicity, only the observations for X and Y are written out in them. The table on the right is the table for the twin planet (all grains of variable X are mature).",
        "ge": "Hier haben wir zwei Tabellen mit Beobachtungen. Der Einfachheit halber sind in ihnen nur die Beobachtungen für X und Y aufgeführt. Die Tabelle auf der rechten Seite ist die Tabelle für den Zwillingsplaneten (alle Körner der Variablen X sind reif).",
    },

    "tab3":{
        "ru": "В данном демонстрационном материале, для того чтобы вам было легче познакомиться с задачей сделаны два упрощения. Все зрелые зерна выделены цветом. Все клумбы находятся не над каменистыми почвами. ",
        "en": "In this demo, to make it easier for you to familiarize yourself with the problem, two simplifications are made. All mature grains are highlighted in color. All beds are not over rocky soils.",
        "ge": "In dieser Demo werden zwei Vereinfachungen vorgenommen, damit Sie sich leichter mit dem Problem vertraut machen können. Alle reifen Körner sind farblich hervorgehoben. Alle Beete befinden sich nicht auf felsigen Böden.",
    },

    "tab4":{
        "ru": "Пожалуйста заполните форму ответа, в соответствии с вашими предположениями о том, какие зависимости между сильными и слабыми растениями следуют из данных таблиц.",
        "en": "Please fill in the answer form according to your assumptions about what relationships between strong and weak plants follow from these tables.",
        "ge": "Füllen Sie bitte das Antwortformular entsprechend Ihren Annahmen darüber aus, welche Beziehungen zwischen starken und schwachen Pflanzen aus diesen Tabellen folgen.",
    },

    "tab12":{
        "ru": "Это последний демо-материал перед переходом к заданию. В нем представлены точно такие-же наблюдения какие демонстрировались прошлый раз, с двумя отличиями.",
        "en": "This is the last demo material before moving on to the task. It presents exactly the same observations as the last demo, with two differences.",
        "ge": "Dies ist das letzte Demomaterial, bevor wir uns der Aufgabe zuwenden. Es enthält genau die gleichen Beobachtungen wie die letzte Demo, mit zwei Unterschieden.",
    },

    "tab22":{
        "ru": "Первое: зрелые семена так же расположены по тем же номерам клумб, но больше нет выделения цветом. Второе: клумба №1 в таблице слева и клумба №3 в таблице справа теперь находятся на каменистых почвах. Обратите внимание, что хоть номера клумб и не совпадают, количество зрелых семян распределённое по каменистым клумбам всегда одинаковое на обоих планетах.",
        "en": "First, the mature seeds are still arranged by the same bed numbers, but there is no more color selection. Second, bed 1 in the table on the left and bed 3 in the table on the right are now on rocky soils. Note that although the bed numbers are not the same, the number of mature seeds distributed on the rocky beds is always the same on both planets.",
        "ge": "Erstens sind die reifen Samen immer noch nach denselben Beetnummern angeordnet, aber es gibt keine Farbauswahl mehr. Zweitens befinden sich Beet 1 in der Tabelle links und Beet 3 in der Tabelle rechts jetzt auf felsigen Böden. Obwohl die Beetnummern nicht gleich sind, ist die Anzahl der reifen Samen, die auf den felsigen Beeten verteilt sind, auf beiden Planeten immer gleich.",
    },

    "carSlide1String1":{
        "ru": "Ваша сессия состоит из "+js_vars.num_rounds+" раундов.  В каждом раунде Вам предстоит выполнять типовые задания, цель и структура которых, не меняется от раунда к раунду.",
        "en": "The session consists of "+js_vars.num_rounds+" rounds. In each round you will be asked to perform identical tasks that do not differ in structure or purpose.",
        "ge": "Die Sitzung besteht aus "+js_vars.num_rounds+" Runden. In jeder Runde werden Sie aufgefordert, identische Aufgaben zu lösen, die sich weder in ihrer Struktur noch in ihrem Zweck unterscheiden.",
    },

    "carSlide1String2":{
        "ru": `Внутри каждого задания вам предстоит ознакомиться с наборами данных, которые разбиты по столбцам (всего 3 столбца). Каждый столбец содержит 16 строк.
               Значение строки в каждом столбце может принимать значения 0 и 1.
               Каждое такое значение является результатом <i>случайного</i> выбора системы,
               однако частота их генерации определяется механизмом, закрепленным за каждым столбцом.`,

        "en": `Inside each assignment you will be given sets of data, which are divided into columns (3 columns in total). Each column contains 16 rows.
               The value of a row in each column can take the values 0 and 1.
               Each such value is the result of a <i>random</i> choice of the system,
               but the frequency of their occurence depends on mechanism assigned to each column.`,

        "ge": `In jeder Aufgabe erhalten Sie Datensätze, die in Spalten unterteilt sind (insgesamt 3 Spalten). Jede Spalte enthält 16 Zeilen.
               Der Wert einer Zeile in jeder Spalte kann die Werte 0 und 1 annehmen.
               Jeder dieser Werte ist das Ergebnis einer <i>zufälligen</i> Wahl des Systems,
               aber die Häufigkeit ihres Auftretens hängt vom Mechanismus ab, der jeder Spalte zugeordnet ist.`,
    },

    "carSlide1String3":{
        "ru": `<b>Частота генерации</b> внутри столбца может зависеть от механизма в другом столбце.
               Это будет означать что если такая зависимость в задании в раунде есть, то значения в столбцах будут генерироваться последовательно, сначала в одном столбце, потом в зависимом от него.`,

        "en": `If the columns are dependent, then in one of them certain values have been randomly selected, and in the other one the <b>generation frequency</b> on the corresponding rows has changed.
               For example, if Y is dependent on X, it may happen that column Y generates a one more often (or less often) on those rows that were also ones in column X.`,

        "ge": `Wenn die Spalten voneinander abhängig sind, dann wurden in einer von ihnen bestimmte Werte zufällig ausgewählt, und in der anderen hat sich die <b>Generierungshäufigkeit</b> in den entsprechenden Zeilen geändert.
               Wenn z. B. Y von X abhängig ist, kann es vorkommen, dass in der Spalte Y häufiger (oder seltener) eine Eins in den Zeilen erscheint, die auch in der Spalte X eine Eins waren.`,
    },

    "carSlide2String1":{
        "ru": `Однако в каждом раунде вам не будет известно есть ли зависимость между столбцами, и в какой последовательности они были сгенерированы (если зависимостей нет, то это не имеет значения).
               Вы будете наблюдать только наборы данных (таблицу с тремя столбцами X, Y и Z) сформированные после того, как система запустит работу механизмов.`,

        "en": `However, in each round, you will not know if there is a dependency between columns, and in what sequence they were generated (if there is no dependency, then it does not matter).
               You will only observe data sets (a table with three columns X, Y and Z) generated after the system runs the mechanisms.`,

        "ge": `In jeder Runde wissen Sie jedoch nicht, ob es eine Abhängigkeit zwischen den Spalten gibt und in welcher Reihenfolge sie erzeugt wurden (wenn es keine Abhängigkeit gibt, spielt es keine Rolle).
               Sie sehen nur die Datensätze (eine Tabelle mit drei Spalten X, Y und Z), die erzeugt werden, nachdem das System die Mechanismen ausgeführt hat.`,
    },

    "carSlide2String2":{
        "ru": `В каждом задании Вы можете перезапустить процесс генерации следующим образом:
              значения в одном из столбцов (Вы будете знать в каком) будут заменены единицами в первую очередь, а после будут определены значения в остальных столбцах.
              Такая операция будет называться DO (название столбца) и для этого будет отдельная кнопка над столбцом.`,

        "en": `In each task you will have the opportunity to start the generation process again as follows:
              the values in one of the columns (you will always know which one) will be changed to ones first, and then the values in the other columns will be determined.
              This operation will be called DO (column name) and there will be a separate button above column.`,

        "ge": `Bei jeder Aufgabe haben Sie die Möglichkeit, den Generierungsprozess wie folgt neu zu starten:
              werden zuerst die Werte in einer der Spalten (Sie wissen immer, welche) in Einsen geändert, und dann werden die Werte in den anderen Spalten ermittelt.
              Dieser Vorgang wird DO (Spaltenname) genannt, und es wird eine separate Schaltfläche über der Spalte geben.`,
    },

    "carSlide3String1":{
        "ru": `Один из элементов управления таблицей позволит Вам отображать только те значения, 
              которые принимает один конкретный столбец, однако это будут те же значения, которые были сгенерированы системой 
              изначально и изменятся будет только их отображение на экране в таблице. Такая операция будет доступна для каждого столбца. 
              Чтобы её совершить нужно будет выставить галочку напротив значения 0 или 1 под названием столбца.
        `,

        "en": `One of the table controls (filter) will allow you to display only the values that one particular column takes.
              But these will be the same values that were originally generated by the system and only their display in the table will change.
              This operation will be available for each column. To do this, you will need to check the box next to the value 0 or 1 under the column name.`,

        "ge": `Eine der Tabellensteuerungen (Filter) ermöglicht es Ihnen, nur die Werte einer bestimmten Spalte anzuzeigen.
              Dabei handelt es sich jedoch um dieselben Werte, die ursprünglich vom System generiert wurden, und nur ihre Anzeige in der Tabelle ändert sich.
              Dieser Vorgang ist für jede Spalte verfügbar. Dazu müssen Sie das Kästchen neben dem Wert 0 oder 1 unter dem Spaltennamen markieren.`,
    },

    "carSlide3String2":{
        "ru": `Задача каждого раунда — определить, зависит ли частота генерации каждого столбца от механизмов генерации в других столбцах.`,

        "en": `The task of each round is to determine whether the frequency of generation of each column depends on the mechanisms in the other columns.`,

        "ge": `Die Aufgabe jeder Runde besteht darin, festzustellen, ob die Häufigkeit der Erzeugung jeder Spalte von den Mechanismen in den anderen Spalten abhängt.`,
    },

    "carSlide3String3":{
        "ru": `В задании последовательность генерации <b>не может</b> быть длиннее трех шагов, т.е. между столбцами не может быть циклов зависимости.
              Это исключает ситуации, в которых, например, столбец X зависит от Y, Y зависит от Z, а Z зависит от X или когда X зависит от Y, а Y зависит от X.`,

        "en": `In this task, the generation sequence <b>cannot be</b> longer than three steps, i.e. there cannot be dependency cycles between columns.
              This eliminates situations where, for example, column X is dependent on Y, Y is dependent on Z and Z is dependent on X, or where X is dependent on Y and Y is dependent on X.`,

        "ge": `Bei dieser Aufgabe darf die Generierungssequenz <b>nicht länger</b> als drei Schritte sein, d.h. es darf keine Abhängigkeitszyklen zwischen den Spalten geben.
              Dadurch werden Situationen vermieden, in denen z. B. Spalte X von Y, Y von Z und Z von X abhängig ist, oder in denen X von Y und Y von X abhängig ist.`,

    },

    "carSlide4String1":{
        "ru": `Из предыдущего абзаца следует, что одновременно может быть верным только одно из следующих утверждений:
              каждый механизм генерации столбцов может либо влиять на другой, либо зависеть от него, либо два механизма не влияют друг на друга.`,

        "en": `It follows from the previous paragraph that only one of the following statements can be true at a time:
              each column generation mechanism can either influence or be dependent on the other one, or two mechanisms do not influence each other.`,

        "ge": `Aus dem vorangegangenen Absatz ergibt sich, dass immer nur eine der folgenden Aussagen wahr sein kann:
              jeder Mechanismus der Spaltenerzeugung kann den anderen entweder beeinflussen oder von ihm abhängig sein, oder zwei Mechanismen beeinflussen sich nicht gegenseitig.`,
    },

    "carSlide4String2":{
        "ru": `Частоты в каждом столбце в этом задании будут сформированы таким образом, что не будет иметь значения, предоставлено ли для их анализа 16 строк или 16 000 строк,
              все закономерности сохраняются.`,

        "en": `The frequencies in each column in this assignment will be generated in such a way that it does not matter whether 16 rows or 16,000 rows are provided for their analysis,
              all patterns will hold.`,

        "ge": `Die Häufigkeiten in jeder Spalte in dieser Aufgabe werden so generiert, dass es keine Rolle spielt, ob 16 Zeilen oder 16.000 Zeilen für ihre Analyse zur Verfügung stehen,
              alle Muster werden beibehalten.`,
    },

    "carSlide4String3":{
        "ru": `Ваш ответ в каждом раунде необходимо будет ввести в графическую форму. В ней каждое имя столбца будет иметь две входящие и две исходящие стрелки (ребра).
              Если Вы считаете, что один из столбцов зависит от другого, Вам нужно будет нажать на стрелку, чтобы сделать ее активной, после чего пунктирная линия превратится в сплошную.`,

        "en": `Your answer in each round, will need to be entered into a graphical form. In it, each column name will have two incoming and two outgoing arrows (edges).
              If you think one of the columns depends on the other, you will need to click on the arrow to make it active, then the dotted line will change to a solid line.`,

        "ge": `Ihre Antwort in jeder Runde muss in ein grafisches Formular eingetragen werden. Darin hat jeder Spaltenname zwei eingehende und zwei ausgehende Pfeile (Kanten).
              Wenn Sie der Meinung sind, dass eine der Spalten von der anderen abhängt, müssen Sie auf den Pfeil klicken, um ihn zu aktivieren; dann wird die gepunktete Linie zu einer durchgezogenen Linie.`,
    },

    "IReadTheSlides":{
        "ru": `С помощью стрелочек < >, Я внимательно прочитал все слайды и понимаю задание.`,

        "en": `Using < > elements, carefully read all slides and understand the task.`,

        "ge": `Ich benutze < > Elemente, lese alle Folien sorgfältig und verstehe die Aufgabe.`,
    },

    "Title":{
        "ru": `Вы можете ознакомиться с записями наблюдений в следующих таблицах:`,

        "en": `You can read the observation records in the following tables:`,

        "ge": `Die Beobachtungssätze können Sie in den folgenden Tabellen nachlesen:`,
    },

    "TrText":{
        "ru": `Давайте разберемся, как заполнять форму!
               Выберите (нажмите) стрелки следующим образом: оставьте ребро пунктирным, если одна переменная не влияет на другую переменную, и сделайте его сплошным, если влияет.
               В качестве примера заполните форму для следующей ситуации: столбец Y зависит от X. После этого нажмите Next.`,

        "en": `Lets figure out how to fill the form!
               Choose (click) the arrows as follows: leave the edge dashed if there is no influence from one variable to another variable and make it solid if there is.
               As an example please fill the form for following situation: column Y are dependent from X. Then tap Next.`,

        "ge": `Lasst uns herausfinden, wie man das Formular ausfüllt!
               Wählen (klicken) Sie die Pfeile wie folgt: Lassen Sie die Kante gestrichelt, wenn es keinen Einfluss von einer Variablen auf eine andere Variable gibt, und machen Sie sie durchgezogen, wenn es einen gibt.
               Als Beispiel füllen Sie bitte das Formular für folgende Situation aus: Spalte Y ist abhängig von X. Tippen Sie dann auf Weiter.`,
    },

    "DtText":{
        "ru": `Пожалуйста, заполните форму ниже`,

        "en": `Please fill in the form below`,

        "ge": `Bitte füllen Sie das untenstehende Formular aus`,
    },

    "confidence":{
        "ru": `Выберите уровень своей уверенности`,

        "en": `Choose your confidence`,

        "ge": `Wählen Sie Ihr Vertrauen`,
    },

    "DTestTitle":{
        "ru": `Результаты предыдущего раунда:`,

        "en": `Results of previous round:`,

        "ge": `Ergebnisse der vorherigen Runde:`,
    },

    "DTestText1":{
        "ru": `То, что было выбрано:`,

        "en": `That what was chosen:`,

        "ge": `Das wurde gewählt:`,
    },

    "DTestText2":{
        "ru": `Те зависимости, на основе которых были сгенерированы данные:`,

        "en": `These dependencies are underlying the basis of the data:`,

        "ge": `Diese Abhängigkeiten bilden die Grundlage für die Daten:`,
    },

    "confstart":{
        "ru": `Используя бегунок укажите, насколько вы уверены в своем ответе`,

        "en": `Please choose how confident you are using slider`,

        "ge": `Bitte wählen Sie, wie sicher Sie den Schieberegler benutzen`,
    },
    "conflevel":{
        "ru": `Текущее значение:`,

        "en": `Current confidience:`,

        "ge": `Derzeitige Vertrautheit:`,
    },
    "Round":{
        "ru": `Планета `,

        "en": `Planet `,

        "ge": `Planet `,
    },

    "Accuracy":{
        "ru": `Ваша точность за этот раунд:`,

        "en": `Your accuracy for the round is`,

        "ge": `Ihre Genauigkeit in der Runde beträgt`,
    },
    "Meanaccuracy":{
        "ru": `Ваша средняя точность за все раунды:`,

        "en": `Your mean accuracy for the rounds is`,

        "ge": `Ihre durchschnittliche Genauigkeit für die Runden beträgt`,
    },
    "Totalscore":{
        "ru": `Сумма выигрыша составила:`,

        "en": `Your total payoff`,

        "ge": `Ihre Gesamtauszahlung`,
    },
    
    "XsYw":{
        "ru": `X - сильное, Y - слабое`,
        "en": `X - strong, Y - weak`,
        "ge": `X - starken, Y - schwache`,
    },

    "XwYs":{
        "ru": `X - слабое, Y - сильное`,
        "en": `X - weak, Y - strong`,
        "ge": `X - schwache, Y - starken`,
    },

    "XYid":{
        "ru": `X и Y нейтральные относительно друг друга`,
        "en": `X and Y are neutral relative to each other`,
        "ge": `X und Y sind relativ zueinander neutral`,
    },

    "XsZw":{
        "ru": `X - сильное, Z - слабое`,
        "en": `X - strong, Z - weak`,
        "ge": `X - starken, Z - schwache`,
    },

    "XwZs":{
        "ru": `X - слабое, Z - сильное`,
        "en": `X - weak, Z - strong`,
        "ge": `X - schwache, Z - starken`,
    },

    "XZid":{
        "ru": `X и Z нейтральные относительно друг друга`,
        "en": `X and Z are neutral relative to each other`,
        "ge": `X und Z sind relativ zueinander neutral`,
    },

    "YsZw":{
        "ru": `Y - сильное, Z - слабое`,
        "en": `Y - strong, Z - weak`,
        "ge": `Y - starken, Z - schwache`,
    },

    "YwZs":{
        "ru": `Y - слабое, Z - сильное`,
        "en": `Y - weak, Z - strong`,
        "ge": `Y - schwache, Z - starken`,
    },

    "YZid":{
        "ru": `Y и Z нейтральные относительно друг друга`,
        "en": `Y and Z are neutral relative to each other`,
        "ge": `Y und Z sind relativ zueinander neutral`,
    },

    "TwinPlanet":{
        "ru": `Планета Близнец`,

        "en": `Twin Planet`,

        "ge": `Planet Zwillinge`,
    },

    "Whatcanttobe":{
        "ru": `Чего <u>не</u> может быть`,

        "en": `What can <u>not</u> to be`,

        "ge": `Das kann <u>nicht</u> sein`,
    },

    "According":{
        "ru": `Согласно данным`,

        "en": `According the data`,

        "ge": `entsprechend den Daten`,
    },

    "Scheme":{
        "ru": `Схема`,

        "en": `Scheme`,

        "ge": `Planen`,
    },

    "Description":{
        "ru": `Описание`,

        "en": `Description`,

        "ge": `Beschreibung`,
    },

    "Cantbe":{
        "ru": `<u>Не</u> может быть`,

        "en": `Can <u>not</u> to be`,

        "ge": `Kann <u>nicht</u> sein`,
    },

    "Cantexclude":{
        "ru": `<u>Нельзя</u> исключать`,

        "en": `Can <u>not</u> exclude`,

        "ge": `Kann <u>nicht</u> ausgeschlossen werden`,
    },

    "Cantbe2":{
        "ru": `<u>Не</u> может быть`,

        "en": `Can <u>not</u> to be`,

        "ge": `Kann <u>nicht</u> sein`,
    },

    "Cantexclude2":{
        "ru": `<u>Нельзя</u> исключать`,

        "en": `Can <u>not</u> exclude`,

        "ge": `Kann <u>nicht</u> ausgeschlossen werden`,
    },

    "Youranswers":{
        "ru": `Ваши ответы`,

        "en": `Your answers`,

        "ge": `Deine Antworten`,
    },

    "Rightanswers":{
        "ru": `Правильные ответы`,

        "en": `Right answers`,

        "ge": `Richtige Antworten`,
    },

    "Prize1":{
        "ru": `Токены, которые Вы получили за соответствие Вашей уверенности и точности выполнения задания:`,

        "en": `Tokens You've got for correspondence of your confidence and task accuracy:`,

        "ge": `NOTRANSLATION`,
    },

    "Prize2":{
        "ru": `Токены, которые Вы получили за точность выполнения задания:`,

        "en": `Tokens You've got for accuracy in task:`,

        "ge": `NOTRANSLATION`,
    },
}
