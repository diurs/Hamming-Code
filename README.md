# Hamming-Code (a systematic coding)

 The Hamming code is self-checking and self-correcting code. Built in relation to the binary number system. Allows you to fix a single error and find a double one. Written in python 3 using the Numpy library.
 
 In this work, a systematic coding is considered, where a systematic code is a code for which the first k characters of a word correspond to message i.
 
The pictures below show the following: x1, x2, x3, x4 - message, a1, a2, a3 - control bits.


 
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

