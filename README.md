# Hamming-Code (a systematic coding)

 The Hamming code is self-checking and self-correcting code. Built in relation to the binary number system. Allows you to fix a single error and find a double one. Written in python 3 using the Numpy library.
 
 In this work, a systematic coding is considered, where a systematic code is a code for which the first k characters of a word correspond to message i.
 
The pictures below show the following: x1, x2, x3, x4 - message, a1, a2, a3 - control bits.

## Блок-схема к программной реализации кодера

![image](https://user-images.githubusercontent.com/61711711/95002290-d46f3780-05da-11eb-87cc-daaf1a93ae10.png)

## Блок-схема к программной реализации декодера

![image](https://user-images.githubusercontent.com/61711711/95002326-3af45580-05db-11eb-9c48-c794af0aa081.png)

 
# Coding algorithm

![image](https://user-images.githubusercontent.com/61711711/95001279-201ce380-05d1-11eb-8739-7d3f8df5e61d.png)


The input receives 4 bits of the original text, then we multiply this vector of the original message by the generating matrix G. As a result of multiplication, we get the encoded text with three control bits at the end.

# Decoding algorithm

![image](https://user-images.githubusercontent.com/61711711/95001314-5195af00-05d1-11eb-934f-fdac2f8f1b02.png)


We have received a message from the sender on a communication channel in which there may be interference. There is a possibility that the transmitted text was distorted as a result of interference. In order to determine if there is an error, multiply F 'by the matrix H and get the syndrome.
Syndrome zero (000) indicates that there are no or no reception errors.
Otherwise, a certain configuration of errors corresponds to any syndrome; they are corrected using a matrix of single errors E. As a result, we get the original text.

# Кодирование

Коды Хэмминга позволяют исправлять одиночную ошибку в блоке. 

Построение кодов Хэмминга основано на принципе проверки на четность числа единичных символов: к последовательности добавляется такой элемент, чтобы число единичных символов в получившейся последовательности было четным.

# Рассмотрим классический код Хемминга (7, 4 ). 

Составим матрицу преобразования, состоящую из 7 столбцов и 3-х строк.
Где количество столбцов - это кол-во битов в закодированном слове, а кол-во строк показывает количество проверочных битов.
Хэмминг предложил построить матрицу следующим образом, где каждый столбец проверочной матрицы будет соответствовать битовому представлению номера разряда числа, которому он соответствует.
Так выглядит данная матрица:

![image](https://user-images.githubusercontent.com/61711711/95001668-c0c0d280-05d4-11eb-82e3-d4e57c8c18d2.png)
 
 
 Эта матрица должна иметь систематический вид, поэтому приведем ее к каноническому виду. Мы переставим в конец столбцы с одной единицей. Тогда матрица H примет вид:
 
 ![image](https://user-images.githubusercontent.com/61711711/95001698-21500f80-05d5-11eb-9427-17af65418c98.png)

Теперь нам нужно построить порождающую матрицу G из матрицы Н.
Проверочная матрица H в каноническом виде имеет вид: H=(An−k,k | En−k), а порождающая матрица G: G = (Ek | A⊤n−k, k). Матрице E принадлежат столбцы с одной единицей => возьмем матрицу А из матрицы H:

![image](https://user-images.githubusercontent.com/61711711/95001718-552b3500-05d5-11eb-9759-450951693ea5.png)

Тогда транспонированная матрица А будет иметь вид:

![image](https://user-images.githubusercontent.com/61711711/95001730-7f7cf280-05d5-11eb-94fa-22f06c6512a2.png)

Ek - матрица со столбцами с одной единицей, где k = числу информационных битов:

![image](https://user-images.githubusercontent.com/61711711/95001789-ed291e80-05d5-11eb-91f5-f8ea1a287f6b.png)


Теперь составим порождающую матрицу G:

![image](https://user-images.githubusercontent.com/61711711/95001791-f4e8c300-05d5-11eb-87d0-c13c9665a14e.png)

Правило формирования проверочных символов составим по вышеупомянутой матрице:

![image](https://user-images.githubusercontent.com/61711711/95001833-658fdf80-05d6-11eb-83e6-457acb8aa65d.png)

Теперь можно произвести алгоритм кодирования:

![image](https://user-images.githubusercontent.com/61711711/95001834-72143800-05d6-11eb-9a8f-4738354c6cee.png)

(i1 i2 i3 i4) - информационные биты, то есть, кодируемый текст, а ( r1 r2 r3 ) - контрольные биты. ( i1 i2 i3 i4 r1 r2 r3 ) - кодовое слово.



## Декодирование

Транспонированная матрица H будет иметь вид:

![image](https://user-images.githubusercontent.com/61711711/95002037-81948080-05d8-11eb-8dd3-ec637346d654.png)

Предположим, что на вход декодера для (7,4)-кода Хэмминга поступает кодовое слово

![image](https://user-images.githubusercontent.com/61711711/95002046-8b1de880-05d8-11eb-9208-65d2026a9ec8.png)
 
Штрих означает, что любой символ слова может быть искажен помехой в канале связи и возникает ошибка E
В декодере в режиме исправления ошибок строится последовательность синдромов:

![image](https://user-images.githubusercontent.com/61711711/95002087-fff12280-05d8-11eb-8257-5f7585454f0e.png)

S = (S1, S2, S3) называется синдромом последовательности.
Получение синдрома происходит по такому выражению:

![image](https://user-images.githubusercontent.com/61711711/95002131-66764080-05d9-11eb-874f-48dba81d16b5.png)

И выглядит следующим образом:

![image](https://user-images.githubusercontent.com/61711711/95002140-81e14b80-05d9-11eb-8201-8bc3de63cf3f.png)

В данном случае синдром S представляет собой сочетание результатов проверки на четность соответствующих символов кодовой группы и характеризует определенную конфигурацию ошибок(вектор ошибок).

Число возможных синдромов определяется выражением 2^3=8
 
При числе проверочных символов  имеется восемь возможных синдромов (2^3 = 8). 

Для определения и исправления искаженного разряда можно использовать матрицу E одиночных ошибок (а можно пользоваться и просто матрицей H 

![image](https://user-images.githubusercontent.com/61711711/95002198-059b3800-05da-11eb-833a-263ccb91c7a4.png)

Данная матрица одиночных ошибок выглядит так:

![image](https://user-images.githubusercontent.com/61711711/95002381-f2896780-05db-11eb-9001-2a9210c3c3f4.png)


При определении синдрома в проверочной матрице находится комбинация синдрома. Искаженный разряд – это разряд в данной строке, в которой стоит «1». Искаженный разряд исправляем посредством сложения строки в матрице ошибок полученной комбинации
