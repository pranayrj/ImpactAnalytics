# Contents
- [Problem Statement](#problem-statement)
- [Approaches](#concepts)
  - [Approache_1](#concept1)
  - [Approache_2](#concept2)
  - [Approache_3](#concept3)
- [How to run](#how-to-run-the-program)

## Problem Statement
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

#### Input
An integer N representing number of days in the academic year

#### Output
Print the following in new line as a string

1. The number of ways to attend classes over N days
2. The probability that you will miss your graduation ceremony

#### Sample Input 1
5

#### Sample Output 1
29

14/29

## CONCEPTS
## Concept_1
Considering the day person is present as "P" and the day he/she is Absent as "A". 
###### Total number of Ways to attend classes over 5 days:
    PPPPP, PPPPA, PPPAP, PPPAA, PPAPP, PPAPA, PPAAP, PPAAA, PAPPP, PAPPA, PAPAP, PAPAA, PAAPP, PAAPA, PAAAP, PAAAA, APPPP, APPPA, APPAP, APPAA, APAPP, APAPA, APAAP, APAAA, AAPPP, AAPPA, AAPAP, AAPAA, AAAPP, AAAPA, AAAAP, AAAAA
    count = 32
###### Invalid Ways to attend classes over 5 days:
    PAAAA, AAAAP, AAAAA
    count = 3
###### Valid Ways to attend classes over 5 days:
    PPPPP, PPPPA, PPPAP, PPPAA, PPAPP, PPAPA, PPAAP, PPAAA, PAPPP, PAPPA, PAPAP, PAPAA, PAAPP, PAAPA, PAAAP, APPPP, APPPA, APPAP, APPAA, APAPP, APAPA, APAAP, APAAA, AAPPP, AAPPA, AAPAP, AAPAA, AAAPP, AAAPA
    count = 29
###### Ways in which the graduation ceremony will be missed i.e. Class is missed on last day:
    PPPPA, PPPAA, PPAPA, PPAAA, PAPPA, PAPAA, PAAPA, APPPA, APPAA, APAPA, APAAA, AAPPA, AAPAA, AAAPA
    count = 14

Therefore, Answer of (1) = 29 , Answer of (2) = 14/29

#### Sample Input 2
7

#### Sample Output 2
108

52/108

### Concept_2
Considering the day person is present as "P" and the day he/she is Absent as "A". 
##### Total number of Ways to attend classes over 7 days:
    PPPPPPP, PPPPPPA, PPPPPAP, PPPPPAA, PPPPAPP, PPPPAPA, PPPPAAP, PPPPAAA, PPPAPPP, PPPAPPA, PPPAPAP, PPPAPAA, PPPAAPP, PPPAAPA, PPPAAAP, PPPAAAA, PPAPPPP, PPAPPPA, PPAPPAP, PPAPPAA, PPAPAPP, PPAPAPA, PPAPAAP, PPAPAAA, PPAAPPP, PPAAPPA, PPAAPAP, PPAAPAA, PPAAAPP, PPAAAPA, PPAAAAP, PPAAAAA, PAPPPPP, PAPPPPA, PAPPPAP, PAPPPAA, PAPPAPP, PAPPAPA, PAPPAAP, PAPPAAA, PAPAPPP, PAPAPPA, PAPAPAP, PAPAPAA, PAPAAPP, PAPAAPA, PAPAAAP, PAPAAAA, PAAPPPP, PAAPPPA, PAAPPAP, PAAPPAA, PAAPAPP, PAAPAPA, PAAPAAP, PAAPAAA, PAAAPPP, PAAAPPA, PAAAPAP, PAAAPAA, PAAAAPP, PAAAAPA, PAAAAAP, PAAAAAA, APPPPPP, APPPPPA, APPPPAP, APPPPAA, APPPAPP, APPPAPA, APPPAAP, APPPAAA, APPAPPP, APPAPPA, APPAPAP, APPAPAA, APPAAPP, APPAAPA, APPAAAP, APPAAAA, APAPPPP, APAPPPA, APAPPAP, APAPPAA, APAPAPP, APAPAPA, APAPAAP, APAPAAA, APAAPPP, APAAPPA, APAAPAP, APAAPAA, APAAAPP, APAAAPA, APAAAAP, APAAAAA, AAPPPPP, AAPPPPA, AAPPPAP, AAPPPAA, AAPPAPP, AAPPAPA, AAPPAAP, AAPPAAA, AAPAPPP, AAPAPPA, AAPAPAP, AAPAPAA, AAPAAPP, AAPAAPA, AAPAAAP, AAPAAAA, AAAPPPP, AAAPPPA, AAAPPAP, AAAPPAA, AAAPAPP, AAAPAPA, AAAPAAP, AAAPAAA, AAAAPPP, AAAAPPA, AAAAPAP, AAAAPAA, AAAAAPP, AAAAAPA, AAAAAAP, AAAAAAA
    count = 128
##### Invalid Ways to attend classes over 7 days:
    PPPAAAA, PPAAAAP, PPAAAAA, PAPAAAA, PAAAAPP, PAAAAPA, PAAAAAP, PAAAAAA, APPAAAA, APAAAAP, APAAAAA, AAPAAAA, AAAAPPP, AAAAPPA, AAAAPAP, AAAAPAA, AAAAAPP, AAAAAPA, AAAAAAP, AAAAAAA
    count = 20
##### Valid Ways to attend classes over 7 days:
    PPPPPPP, PPPPPPA, PPPPPAP, PPPPPAA, PPPPAPP, PPPPAPA, PPPPAAP, PPPPAAA, PPPAPPP, PPPAPPA, PPPAPAP, PPPAPAA, PPPAAPP, PPPAAPA, PPPAAAP, PPAPPPP, PPAPPPA, PPAPPAP, PPAPPAA, PPAPAPP, PPAPAPA, PPAPAAP, PPAPAAA, PPAAPPP, PPAAPPA, PPAAPAP, PPAAPAA, PPAAAPP, PPAAAPA, PAPPPPP, PAPPPPA, PAPPPAP, PAPPPAA, PAPPAPP, PAPPAPA, PAPPAAP, PAPPAAA, PAPAPPP, PAPAPPA, PAPAPAP, PAPAPAA, PAPAAPP, PAPAAPA, PAPAAAP, PAAPPPP, PAAPPPA, PAAPPAP, PAAPPAA, PAAPAPP, PAAPAPA, PAAPAAP, PAAPAAA, PAAAPPP, PAAAPPA, PAAAPAP, PAAAPAA, APPPPPP, APPPPPA, APPPPAP, APPPPAA, APPPAPP, APPPAPA, APPPAAP, APPPAAA, APPAPPP, APPAPPA, APPAPAP, APPAPAA, APPAAPP, APPAAPA, APPAAAP, APAPPPP, APAPPPA, APAPPAP, APAPPAA, APAPAPP, APAPAPA, APAPAAP, APAPAAA, APAAPPP, APAAPPA, APAAPAP, APAAPAA, APAAAPP, APAAAPA, AAPPPPP, AAPPPPA, AAPPPAP, AAPPPAA, AAPPAPP, AAPPAPA, AAPPAAP, AAPPAAA, AAPAPPP, AAPAPPA, AAPAPAP, AAPAPAA, AAPAAPP, AAPAAPA, AAPAAAP, AAAPPPP, AAAPPPA, AAAPPAP, AAAPPAA, AAAPAPP, AAAPAPA, AAAPAAP, AAAPAAA
    count = 108
##### Ways in which the graduation ceremony will be missed i.e. Class is missed on last day:
    PPPPPPA, PPPPPAA, PPPPAPA, PPPPAAA, PPPAPPA, PPPAPAA, PPPAAPA, PPAPPPA, PPAPPAA, PPAPAPA, PPAPAAA, PPAAPPA, PPAAPAA, PPAAAPA, PAPPPPA, PAPPPAA, PAPPAPA, PAPPAAA, PAPAPPA, PAPAPAA, PAPAAPA, PAAPPPA, PAAPPAA, PAAPAPA, PAAPAAA, PAAAPPA, PAAAPAA, APPPPPA, APPPPAA, APPPAPA, APPPAAA, APPAPPA, APPAPAA, APPAAPA, APAPPPA, APAPPAA, APAPAPA, APAPAAA, APAAPPA, APAAPAA, APAAAPA, AAPPPPA, AAPPPAA, AAPPAPA, AAPPAAA, AAPAPPA, AAPAPAA, AAPAAPA, AAAPPPA, AAAPPAA, AAAPAPA, AAAPAAA
    count = 52

Therefore, Answer of (1) = 108 , Answer of (2) = 52/108

#### Sample Input 3
10

#### Sample Output 3
773

372/773

### Concept_3
Considering the day person is present as "P" and the day he/she is Absent as "A".  
##### Total number of Ways to attend classes over 10 days:
    PPPPPPPPPP, PPPPPPPPPA, PPPPPPPPAP, PPPPPPPPAA, PPPPPPPAPP, PPPPPPPAPA, PPPPPPPAAP, PPPPPPPAAA, PPPPPPAPPP, PPPPPPAPPA, PPPPPPAPAP, PPPPPPAPAA, PPPPPPAAPP, PPPPPPAAPA, PPPPPPAAAP, PPPPPPAAAA, PPPPPAPPPP, PPPPPAPPPA, PPPPPAPPAP, PPPPPAPPAA, PPPPPAPAPP, PPPPPAPAPA, PPPPPAPAAP, PPPPPAPAAA, PPPPPAAPPP, PPPPPAAPPA, PPPPPAAPAP, PPPPPAAPAA, PPPPPAAAPP, PPPPPAAAPA, PPPPPAAAAP, PPPPPAAAAA, PPPPAPPPPP, PPPPAPPPPA, PPPPAPPPAP, PPPPAPPPAA, PPPPAPPAPP, PPPPAPPAPA, PPPPAPPAAP, PPPPAPPAAA, PPPPAPAPPP, PPPPAPAPPA, PPPPAPAPAP, PPPPAPAPAA, PPPPAPAAPP, PPPPAPAAPA, PPPPAPAAAP, PPPPAPAAAA, PPPPAAPPPP, PPPPAAPPPA, PPPPAAPPAP, PPPPAAPPAA, PPPPAAPAPP, PPPPAAPAPA, PPPPAAPAAP, PPPPAAPAAA, PPPPAAAPPP, PPPPAAAPPA, PPPPAAAPAP, PPPPAAAPAA, PPPPAAAAPP, PPPPAAAAPA, PPPPAAAAAP, PPPPAAAAAA, PPPAPPPPPP, PPPAPPPPPA, PPPAPPPPAP, PPPAPPPPAA, PPPAPPPAPP, PPPAPPPAPA, PPPAPPPAAP, PPPAPPPAAA, PPPAPPAPPP, PPPAPPAPPA, PPPAPPAPAP, PPPAPPAPAA, PPPAPPAAPP, PPPAPPAAPA, PPPAPPAAAP, PPPAPPAAAA, PPPAPAPPPP, PPPAPAPPPA, PPPAPAPPAP, PPPAPAPPAA, PPPAPAPAPP, PPPAPAPAPA, PPPAPAPAAP, PPPAPAPAAA, PPPAPAAPPP, PPPAPAAPPA, PPPAPAAPAP, PPPAPAAPAA, PPPAPAAAPP, PPPAPAAAPA, PPPAPAAAAP, PPPAPAAAAA, PPPAAPPPPP, PPPAAPPPPA, PPPAAPPPAP, PPPAAPPPAA, PPPAAPPAPP, PPPAAPPAPA, PPPAAPPAAP, PPPAAPPAAA, PPPAAPAPPP, PPPAAPAPPA, PPPAAPAPAP, PPPAAPAPAA, PPPAAPAAPP, PPPAAPAAPA, PPPAAPAAAP, PPPAAPAAAA, PPPAAAPPPP, PPPAAAPPPA, PPPAAAPPAP, PPPAAAPPAA, PPPAAAPAPP, PPPAAAPAPA, PPPAAAPAAP, PPPAAAPAAA, PPPAAAAPPP, PPPAAAAPPA, PPPAAAAPAP, PPPAAAAPAA, PPPAAAAAPP, PPPAAAAAPA, PPPAAAAAAP, PPPAAAAAAA, PPAPPPPPPP, PPAPPPPPPA, PPAPPPPPAP, PPAPPPPPAA, PPAPPPPAPP, PPAPPPPAPA, PPAPPPPAAP, PPAPPPPAAA, PPAPPPAPPP, PPAPPPAPPA, PPAPPPAPAP, PPAPPPAPAA, PPAPPPAAPP, PPAPPPAAPA, PPAPPPAAAP, PPAPPPAAAA, PPAPPAPPPP, PPAPPAPPPA, PPAPPAPPAP, PPAPPAPPAA, PPAPPAPAPP, PPAPPAPAPA, PPAPPAPAAP, PPAPPAPAAA, PPAPPAAPPP, PPAPPAAPPA, PPAPPAAPAP, PPAPPAAPAA, PPAPPAAAPP, PPAPPAAAPA, PPAPPAAAAP, PPAPPAAAAA, PPAPAPPPPP, PPAPAPPPPA, PPAPAPPPAP, PPAPAPPPAA, PPAPAPPAPP, PPAPAPPAPA, PPAPAPPAAP, PPAPAPPAAA, PPAPAPAPPP, PPAPAPAPPA, PPAPAPAPAP, PPAPAPAPAA, PPAPAPAAPP, PPAPAPAAPA, PPAPAPAAAP, PPAPAPAAAA, PPAPAAPPPP, PPAPAAPPPA, PPAPAAPPAP, PPAPAAPPAA, PPAPAAPAPP, PPAPAAPAPA, PPAPAAPAAP, PPAPAAPAAA, PPAPAAAPPP, PPAPAAAPPA, PPAPAAAPAP, PPAPAAAPAA, PPAPAAAAPP, PPAPAAAAPA, PPAPAAAAAP, PPAPAAAAAA, PPAAPPPPPP, PPAAPPPPPA, PPAAPPPPAP, PPAAPPPPAA, PPAAPPPAPP, PPAAPPPAPA, PPAAPPPAAP, PPAAPPPAAA, PPAAPPAPPP, PPAAPPAPPA, PPAAPPAPAP, PPAAPPAPAA, PPAAPPAAPP, PPAAPPAAPA, PPAAPPAAAP, PPAAPPAAAA, PPAAPAPPPP, PPAAPAPPPA, PPAAPAPPAP, PPAAPAPPAA, PPAAPAPAPP, PPAAPAPAPA, PPAAPAPAAP, PPAAPAPAAA, PPAAPAAPPP, PPAAPAAPPA, PPAAPAAPAP, PPAAPAAPAA, PPAAPAAAPP, PPAAPAAAPA, PPAAPAAAAP, PPAAPAAAAA, PPAAAPPPPP, PPAAAPPPPA, PPAAAPPPAP, PPAAAPPPAA, PPAAAPPAPP, PPAAAPPAPA, PPAAAPPAAP, PPAAAPPAAA, PPAAAPAPPP, PPAAAPAPPA, PPAAAPAPAP, PPAAAPAPAA, PPAAAPAAPP, PPAAAPAAPA, PPAAAPAAAP, PPAAAPAAAA, PPAAAAPPPP, PPAAAAPPPA, PPAAAAPPAP, PPAAAAPPAA, PPAAAAPAPP, PPAAAAPAPA, PPAAAAPAAP, PPAAAAPAAA, PPAAAAAPPP, PPAAAAAPPA, PPAAAAAPAP, PPAAAAAPAA, PPAAAAAAPP, PPAAAAAAPA, PPAAAAAAAP, PPAAAAAAAA, PAPPPPPPPP, PAPPPPPPPA, PAPPPPPPAP, PAPPPPPPAA, PAPPPPPAPP, PAPPPPPAPA, PAPPPPPAAP, PAPPPPPAAA, PAPPPPAPPP, PAPPPPAPPA, PAPPPPAPAP, PAPPPPAPAA, PAPPPPAAPP, PAPPPPAAPA, PAPPPPAAAP, PAPPPPAAAA, PAPPPAPPPP, PAPPPAPPPA, PAPPPAPPAP, PAPPPAPPAA, PAPPPAPAPP, PAPPPAPAPA, PAPPPAPAAP, PAPPPAPAAA, PAPPPAAPPP, PAPPPAAPPA, PAPPPAAPAP, PAPPPAAPAA, PAPPPAAAPP, PAPPPAAAPA, PAPPPAAAAP, PAPPPAAAAA, PAPPAPPPPP, PAPPAPPPPA, PAPPAPPPAP, PAPPAPPPAA, PAPPAPPAPP, PAPPAPPAPA, PAPPAPPAAP, PAPPAPPAAA, PAPPAPAPPP, PAPPAPAPPA, PAPPAPAPAP, PAPPAPAPAA, PAPPAPAAPP, PAPPAPAAPA, PAPPAPAAAP, PAPPAPAAAA, PAPPAAPPPP, PAPPAAPPPA, PAPPAAPPAP, PAPPAAPPAA, PAPPAAPAPP, PAPPAAPAPA, PAPPAAPAAP, PAPPAAPAAA, PAPPAAAPPP, PAPPAAAPPA, PAPPAAAPAP, PAPPAAAPAA, PAPPAAAAPP, PAPPAAAAPA, PAPPAAAAAP, PAPPAAAAAA, PAPAPPPPPP, PAPAPPPPPA, PAPAPPPPAP, PAPAPPPPAA, PAPAPPPAPP, PAPAPPPAPA, PAPAPPPAAP, PAPAPPPAAA, PAPAPPAPPP, PAPAPPAPPA, PAPAPPAPAP, PAPAPPAPAA, PAPAPPAAPP, PAPAPPAAPA, PAPAPPAAAP, PAPAPPAAAA, PAPAPAPPPP, PAPAPAPPPA, PAPAPAPPAP, PAPAPAPPAA, PAPAPAPAPP, PAPAPAPAPA, PAPAPAPAAP, PAPAPAPAAA, PAPAPAAPPP, PAPAPAAPPA, PAPAPAAPAP, PAPAPAAPAA, PAPAPAAAPP, PAPAPAAAPA, PAPAPAAAAP, PAPAPAAAAA, PAPAAPPPPP, PAPAAPPPPA, PAPAAPPPAP, PAPAAPPPAA, PAPAAPPAPP, PAPAAPPAPA, PAPAAPPAAP, PAPAAPPAAA, PAPAAPAPPP, PAPAAPAPPA, PAPAAPAPAP, PAPAAPAPAA, PAPAAPAAPP, PAPAAPAAPA, PAPAAPAAAP, PAPAAPAAAA, PAPAAAPPPP, PAPAAAPPPA, PAPAAAPPAP, PAPAAAPPAA, PAPAAAPAPP, PAPAAAPAPA, PAPAAAPAAP, PAPAAAPAAA, PAPAAAAPPP, PAPAAAAPPA, PAPAAAAPAP, PAPAAAAPAA, PAPAAAAAPP, PAPAAAAAPA, PAPAAAAAAP, PAPAAAAAAA, PAAPPPPPPP, PAAPPPPPPA, PAAPPPPPAP, PAAPPPPPAA, PAAPPPPAPP, PAAPPPPAPA, PAAPPPPAAP, PAAPPPPAAA, PAAPPPAPPP, PAAPPPAPPA, PAAPPPAPAP, PAAPPPAPAA, PAAPPPAAPP, PAAPPPAAPA, PAAPPPAAAP, PAAPPPAAAA, PAAPPAPPPP, PAAPPAPPPA, PAAPPAPPAP, PAAPPAPPAA, PAAPPAPAPP, PAAPPAPAPA, PAAPPAPAAP, PAAPPAPAAA, PAAPPAAPPP, PAAPPAAPPA, PAAPPAAPAP, PAAPPAAPAA, PAAPPAAAPP, PAAPPAAAPA, PAAPPAAAAP, PAAPPAAAAA, PAAPAPPPPP, PAAPAPPPPA, PAAPAPPPAP, PAAPAPPPAA, PAAPAPPAPP, PAAPAPPAPA, PAAPAPPAAP, PAAPAPPAAA, PAAPAPAPPP, PAAPAPAPPA, PAAPAPAPAP, PAAPAPAPAA, PAAPAPAAPP, PAAPAPAAPA, PAAPAPAAAP, PAAPAPAAAA, PAAPAAPPPP, PAAPAAPPPA, PAAPAAPPAP, PAAPAAPPAA, PAAPAAPAPP, PAAPAAPAPA, PAAPAAPAAP, PAAPAAPAAA, PAAPAAAPPP, PAAPAAAPPA, PAAPAAAPAP, PAAPAAAPAA, PAAPAAAAPP, PAAPAAAAPA, PAAPAAAAAP, PAAPAAAAAA, PAAAPPPPPP, PAAAPPPPPA, PAAAPPPPAP, PAAAPPPPAA, PAAAPPPAPP, PAAAPPPAPA, PAAAPPPAAP, PAAAPPPAAA, PAAAPPAPPP, PAAAPPAPPA, PAAAPPAPAP, PAAAPPAPAA, PAAAPPAAPP, PAAAPPAAPA, PAAAPPAAAP, PAAAPPAAAA, PAAAPAPPPP, PAAAPAPPPA, PAAAPAPPAP, PAAAPAPPAA, PAAAPAPAPP, PAAAPAPAPA, PAAAPAPAAP, PAAAPAPAAA, PAAAPAAPPP, PAAAPAAPPA, PAAAPAAPAP, PAAAPAAPAA, PAAAPAAAPP, PAAAPAAAPA, PAAAPAAAAP, PAAAPAAAAA, PAAAAPPPPP, PAAAAPPPPA, PAAAAPPPAP, PAAAAPPPAA, PAAAAPPAPP, PAAAAPPAPA, PAAAAPPAAP, PAAAAPPAAA, PAAAAPAPPP, PAAAAPAPPA, PAAAAPAPAP, PAAAAPAPAA, PAAAAPAAPP, PAAAAPAAPA, PAAAAPAAAP, PAAAAPAAAA, PAAAAAPPPP, PAAAAAPPPA, PAAAAAPPAP, PAAAAAPPAA, PAAAAAPAPP, PAAAAAPAPA, PAAAAAPAAP, PAAAAAPAAA, PAAAAAAPPP, PAAAAAAPPA, PAAAAAAPAP, PAAAAAAPAA, PAAAAAAAPP, PAAAAAAAPA, PAAAAAAAAP, PAAAAAAAAA, APPPPPPPPP, APPPPPPPPA, APPPPPPPAP, APPPPPPPAA, APPPPPPAPP, APPPPPPAPA, APPPPPPAAP, APPPPPPAAA, APPPPPAPPP, APPPPPAPPA, APPPPPAPAP, APPPPPAPAA, APPPPPAAPP, APPPPPAAPA, APPPPPAAAP, APPPPPAAAA, APPPPAPPPP, APPPPAPPPA, APPPPAPPAP, APPPPAPPAA, APPPPAPAPP, APPPPAPAPA, APPPPAPAAP, APPPPAPAAA, APPPPAAPPP, APPPPAAPPA, APPPPAAPAP, APPPPAAPAA, APPPPAAAPP, APPPPAAAPA, APPPPAAAAP, APPPPAAAAA, APPPAPPPPP, APPPAPPPPA, APPPAPPPAP, APPPAPPPAA, APPPAPPAPP, APPPAPPAPA, APPPAPPAAP, APPPAPPAAA, APPPAPAPPP, APPPAPAPPA, APPPAPAPAP, APPPAPAPAA, APPPAPAAPP, APPPAPAAPA, APPPAPAAAP, APPPAPAAAA, APPPAAPPPP, APPPAAPPPA, APPPAAPPAP, APPPAAPPAA, APPPAAPAPP, APPPAAPAPA, APPPAAPAAP, APPPAAPAAA, APPPAAAPPP, APPPAAAPPA, APPPAAAPAP, APPPAAAPAA, APPPAAAAPP, APPPAAAAPA, APPPAAAAAP, APPPAAAAAA, APPAPPPPPP, APPAPPPPPA, APPAPPPPAP, APPAPPPPAA, APPAPPPAPP, APPAPPPAPA, APPAPPPAAP, APPAPPPAAA, APPAPPAPPP, APPAPPAPPA, APPAPPAPAP, APPAPPAPAA, APPAPPAAPP, APPAPPAAPA, APPAPPAAAP, APPAPPAAAA, APPAPAPPPP, APPAPAPPPA, APPAPAPPAP, APPAPAPPAA, APPAPAPAPP, APPAPAPAPA, APPAPAPAAP, APPAPAPAAA, APPAPAAPPP, APPAPAAPPA, APPAPAAPAP, APPAPAAPAA, APPAPAAAPP, APPAPAAAPA, APPAPAAAAP, APPAPAAAAA, APPAAPPPPP, APPAAPPPPA, APPAAPPPAP, APPAAPPPAA, APPAAPPAPP, APPAAPPAPA, APPAAPPAAP, APPAAPPAAA, APPAAPAPPP, APPAAPAPPA, APPAAPAPAP, APPAAPAPAA, APPAAPAAPP, APPAAPAAPA, APPAAPAAAP, APPAAPAAAA, APPAAAPPPP, APPAAAPPPA, APPAAAPPAP, APPAAAPPAA, APPAAAPAPP, APPAAAPAPA, APPAAAPAAP, APPAAAPAAA, APPAAAAPPP, APPAAAAPPA, APPAAAAPAP, APPAAAAPAA, APPAAAAAPP, APPAAAAAPA, APPAAAAAAP, APPAAAAAAA, APAPPPPPPP, APAPPPPPPA, APAPPPPPAP, APAPPPPPAA, APAPPPPAPP, APAPPPPAPA, APAPPPPAAP, APAPPPPAAA, APAPPPAPPP, APAPPPAPPA, APAPPPAPAP, APAPPPAPAA, APAPPPAAPP, APAPPPAAPA, APAPPPAAAP, APAPPPAAAA, APAPPAPPPP, APAPPAPPPA, APAPPAPPAP, APAPPAPPAA, APAPPAPAPP, APAPPAPAPA, APAPPAPAAP, APAPPAPAAA, APAPPAAPPP, APAPPAAPPA, APAPPAAPAP, APAPPAAPAA, APAPPAAAPP, APAPPAAAPA, APAPPAAAAP, APAPPAAAAA, APAPAPPPPP, APAPAPPPPA, APAPAPPPAP, APAPAPPPAA, APAPAPPAPP, APAPAPPAPA, APAPAPPAAP, APAPAPPAAA, APAPAPAPPP, APAPAPAPPA, APAPAPAPAP, APAPAPAPAA, APAPAPAAPP, APAPAPAAPA, APAPAPAAAP, APAPAPAAAA, APAPAAPPPP, APAPAAPPPA, APAPAAPPAP, APAPAAPPAA, APAPAAPAPP, APAPAAPAPA, APAPAAPAAP, APAPAAPAAA, APAPAAAPPP, APAPAAAPPA, APAPAAAPAP, APAPAAAPAA, APAPAAAAPP, APAPAAAAPA, APAPAAAAAP, APAPAAAAAA, APAAPPPPPP, APAAPPPPPA, APAAPPPPAP, APAAPPPPAA, APAAPPPAPP, APAAPPPAPA, APAAPPPAAP, APAAPPPAAA, APAAPPAPPP, APAAPPAPPA, APAAPPAPAP, APAAPPAPAA, APAAPPAAPP, APAAPPAAPA, APAAPPAAAP, APAAPPAAAA, APAAPAPPPP, APAAPAPPPA, APAAPAPPAP, APAAPAPPAA, APAAPAPAPP, APAAPAPAPA, APAAPAPAAP, APAAPAPAAA, APAAPAAPPP, APAAPAAPPA, APAAPAAPAP, APAAPAAPAA, APAAPAAAPP, APAAPAAAPA, APAAPAAAAP, APAAPAAAAA, APAAAPPPPP, APAAAPPPPA, APAAAPPPAP, APAAAPPPAA, APAAAPPAPP, APAAAPPAPA, APAAAPPAAP, APAAAPPAAA, APAAAPAPPP, APAAAPAPPA, APAAAPAPAP, APAAAPAPAA, APAAAPAAPP, APAAAPAAPA, APAAAPAAAP, APAAAPAAAA, APAAAAPPPP, APAAAAPPPA, APAAAAPPAP, APAAAAPPAA, APAAAAPAPP, APAAAAPAPA, APAAAAPAAP, APAAAAPAAA, APAAAAAPPP, APAAAAAPPA, APAAAAAPAP, APAAAAAPAA, APAAAAAAPP, APAAAAAAPA, APAAAAAAAP, APAAAAAAAA, AAPPPPPPPP, AAPPPPPPPA, AAPPPPPPAP, AAPPPPPPAA, AAPPPPPAPP, AAPPPPPAPA, AAPPPPPAAP, AAPPPPPAAA, AAPPPPAPPP, AAPPPPAPPA, AAPPPPAPAP, AAPPPPAPAA, AAPPPPAAPP, AAPPPPAAPA, AAPPPPAAAP, AAPPPPAAAA, AAPPPAPPPP, AAPPPAPPPA, AAPPPAPPAP, AAPPPAPPAA, AAPPPAPAPP, AAPPPAPAPA, AAPPPAPAAP, AAPPPAPAAA, AAPPPAAPPP, AAPPPAAPPA, AAPPPAAPAP, AAPPPAAPAA, AAPPPAAAPP, AAPPPAAAPA, AAPPPAAAAP, AAPPPAAAAA, AAPPAPPPPP, AAPPAPPPPA, AAPPAPPPAP, AAPPAPPPAA, AAPPAPPAPP, AAPPAPPAPA, AAPPAPPAAP, AAPPAPPAAA, AAPPAPAPPP, AAPPAPAPPA, AAPPAPAPAP, AAPPAPAPAA, AAPPAPAAPP, AAPPAPAAPA, AAPPAPAAAP, AAPPAPAAAA, AAPPAAPPPP, AAPPAAPPPA, AAPPAAPPAP, AAPPAAPPAA, AAPPAAPAPP, AAPPAAPAPA, AAPPAAPAAP, AAPPAAPAAA, AAPPAAAPPP, AAPPAAAPPA, AAPPAAAPAP, AAPPAAAPAA, AAPPAAAAPP, AAPPAAAAPA, AAPPAAAAAP, AAPPAAAAAA, AAPAPPPPPP, AAPAPPPPPA, AAPAPPPPAP, AAPAPPPPAA, AAPAPPPAPP, AAPAPPPAPA, AAPAPPPAAP, AAPAPPPAAA, AAPAPPAPPP, AAPAPPAPPA, AAPAPPAPAP, AAPAPPAPAA, AAPAPPAAPP, AAPAPPAAPA, AAPAPPAAAP, AAPAPPAAAA, AAPAPAPPPP, AAPAPAPPPA, AAPAPAPPAP, AAPAPAPPAA, AAPAPAPAPP, AAPAPAPAPA, AAPAPAPAAP, AAPAPAPAAA, AAPAPAAPPP, AAPAPAAPPA, AAPAPAAPAP, AAPAPAAPAA, AAPAPAAAPP, AAPAPAAAPA, AAPAPAAAAP, AAPAPAAAAA, AAPAAPPPPP, AAPAAPPPPA, AAPAAPPPAP, AAPAAPPPAA, AAPAAPPAPP, AAPAAPPAPA, AAPAAPPAAP, AAPAAPPAAA, AAPAAPAPPP, AAPAAPAPPA, AAPAAPAPAP, AAPAAPAPAA, AAPAAPAAPP, AAPAAPAAPA, AAPAAPAAAP, AAPAAPAAAA, AAPAAAPPPP, AAPAAAPPPA, AAPAAAPPAP, AAPAAAPPAA, AAPAAAPAPP, AAPAAAPAPA, AAPAAAPAAP, AAPAAAPAAA, AAPAAAAPPP, AAPAAAAPPA, AAPAAAAPAP, AAPAAAAPAA, AAPAAAAAPP, AAPAAAAAPA, AAPAAAAAAP, AAPAAAAAAA, AAAPPPPPPP, AAAPPPPPPA, AAAPPPPPAP, AAAPPPPPAA, AAAPPPPAPP, AAAPPPPAPA, AAAPPPPAAP, AAAPPPPAAA, AAAPPPAPPP, AAAPPPAPPA, AAAPPPAPAP, AAAPPPAPAA, AAAPPPAAPP, AAAPPPAAPA, AAAPPPAAAP, AAAPPPAAAA, AAAPPAPPPP, AAAPPAPPPA, AAAPPAPPAP, AAAPPAPPAA, AAAPPAPAPP, AAAPPAPAPA, AAAPPAPAAP, AAAPPAPAAA, AAAPPAAPPP, AAAPPAAPPA, AAAPPAAPAP, AAAPPAAPAA, AAAPPAAAPP, AAAPPAAAPA, AAAPPAAAAP, AAAPPAAAAA, AAAPAPPPPP, AAAPAPPPPA, AAAPAPPPAP, AAAPAPPPAA, AAAPAPPAPP, AAAPAPPAPA, AAAPAPPAAP, AAAPAPPAAA, AAAPAPAPPP, AAAPAPAPPA, AAAPAPAPAP, AAAPAPAPAA, AAAPAPAAPP, AAAPAPAAPA, AAAPAPAAAP, AAAPAPAAAA, AAAPAAPPPP, AAAPAAPPPA, AAAPAAPPAP, AAAPAAPPAA, AAAPAAPAPP, AAAPAAPAPA, AAAPAAPAAP, AAAPAAPAAA, AAAPAAAPPP, AAAPAAAPPA, AAAPAAAPAP, AAAPAAAPAA, AAAPAAAAPP, AAAPAAAAPA, AAAPAAAAAP, AAAPAAAAAA, AAAAPPPPPP, AAAAPPPPPA, AAAAPPPPAP, AAAAPPPPAA, AAAAPPPAPP, AAAAPPPAPA, AAAAPPPAAP, AAAAPPPAAA, AAAAPPAPPP, AAAAPPAPPA, AAAAPPAPAP, AAAAPPAPAA, AAAAPPAAPP, AAAAPPAAPA, AAAAPPAAAP, AAAAPPAAAA, AAAAPAPPPP, AAAAPAPPPA, AAAAPAPPAP, AAAAPAPPAA, AAAAPAPAPP, AAAAPAPAPA, AAAAPAPAAP, AAAAPAPAAA, AAAAPAAPPP, AAAAPAAPPA, AAAAPAAPAP, AAAAPAAPAA, AAAAPAAAPP, AAAAPAAAPA, AAAAPAAAAP, AAAAPAAAAA, AAAAAPPPPP, AAAAAPPPPA, AAAAAPPPAP, AAAAAPPPAA, AAAAAPPAPP, AAAAAPPAPA, AAAAAPPAAP, AAAAAPPAAA, AAAAAPAPPP, AAAAAPAPPA, AAAAAPAPAP, AAAAAPAPAA, AAAAAPAAPP, AAAAAPAAPA, AAAAAPAAAP, AAAAAPAAAA, AAAAAAPPPP, AAAAAAPPPA, AAAAAAPPAP, AAAAAAPPAA, AAAAAAPAPP, AAAAAAPAPA, AAAAAAPAAP, AAAAAAPAAA, AAAAAAAPPP, AAAAAAAPPA, AAAAAAAPAP, AAAAAAAPAA, AAAAAAAAPP, AAAAAAAAPA, AAAAAAAAAP, AAAAAAAAAA
    count = 1024
##### Invalid Ways to attend classes over 10 days:
    PPPPPPAAAA, PPPPPAAAAP, PPPPPAAAAA, PPPPAPAAAA, PPPPAAAAPP, PPPPAAAAPA, PPPPAAAAAP, PPPPAAAAAA, PPPAPPAAAA, PPPAPAAAAP, PPPAPAAAAA, PPPAAPAAAA, PPPAAAAPPP, PPPAAAAPPA, PPPAAAAPAP, PPPAAAAPAA, PPPAAAAAPP, PPPAAAAAPA, PPPAAAAAAP, PPPAAAAAAA, PPAPPPAAAA, PPAPPAAAAP, PPAPPAAAAA, PPAPAPAAAA, PPAPAAAAPP, PPAPAAAAPA, PPAPAAAAAP, PPAPAAAAAA, PPAAPPAAAA, PPAAPAAAAP, PPAAPAAAAA, PPAAAPAAAA, PPAAAAPPPP, PPAAAAPPPA, PPAAAAPPAP, PPAAAAPPAA, PPAAAAPAPP, PPAAAAPAPA, PPAAAAPAAP, PPAAAAPAAA, PPAAAAAPPP, PPAAAAAPPA, PPAAAAAPAP, PPAAAAAPAA, PPAAAAAAPP, PPAAAAAAPA, PPAAAAAAAP, PPAAAAAAAA, PAPPPPAAAA, PAPPPAAAAP, PAPPPAAAAA, PAPPAPAAAA, PAPPAAAAPP, PAPPAAAAPA, PAPPAAAAAP, PAPPAAAAAA, PAPAPPAAAA, PAPAPAAAAP, PAPAPAAAAA, PAPAAPAAAA, PAPAAAAPPP, PAPAAAAPPA, PAPAAAAPAP, PAPAAAAPAA, PAPAAAAAPP, PAPAAAAAPA, PAPAAAAAAP, PAPAAAAAAA, PAAPPPAAAA, PAAPPAAAAP, PAAPPAAAAA, PAAPAPAAAA, PAAPAAAAPP, PAAPAAAAPA, PAAPAAAAAP, PAAPAAAAAA, PAAAPPAAAA, PAAAPAAAAP, PAAAPAAAAA, PAAAAPPPPP, PAAAAPPPPA, PAAAAPPPAP, PAAAAPPPAA, PAAAAPPAPP, PAAAAPPAPA, PAAAAPPAAP, PAAAAPPAAA, PAAAAPAPPP, PAAAAPAPPA, PAAAAPAPAP, PAAAAPAPAA, PAAAAPAAPP, PAAAAPAAPA, PAAAAPAAAP, PAAAAPAAAA, PAAAAAPPPP, PAAAAAPPPA, PAAAAAPPAP, PAAAAAPPAA, PAAAAAPAPP, PAAAAAPAPA, PAAAAAPAAP, PAAAAAPAAA, PAAAAAAPPP, PAAAAAAPPA, PAAAAAAPAP, PAAAAAAPAA, PAAAAAAAPP, PAAAAAAAPA, PAAAAAAAAP, PAAAAAAAAA, APPPPPAAAA, APPPPAAAAP, APPPPAAAAA, APPPAPAAAA, APPPAAAAPP, APPPAAAAPA, APPPAAAAAP, APPPAAAAAA, APPAPPAAAA, APPAPAAAAP, APPAPAAAAA, APPAAPAAAA, APPAAAAPPP, APPAAAAPPA, APPAAAAPAP, APPAAAAPAA, APPAAAAAPP, APPAAAAAPA, APPAAAAAAP, APPAAAAAAA, APAPPPAAAA, APAPPAAAAP, APAPPAAAAA, APAPAPAAAA, APAPAAAAPP, APAPAAAAPA, APAPAAAAAP, APAPAAAAAA, APAAPPAAAA, APAAPAAAAP, APAAPAAAAA, APAAAPAAAA, APAAAAPPPP, APAAAAPPPA, APAAAAPPAP, APAAAAPPAA, APAAAAPAPP, APAAAAPAPA, APAAAAPAAP, APAAAAPAAA, APAAAAAPPP, APAAAAAPPA, APAAAAAPAP, APAAAAAPAA, APAAAAAAPP, APAAAAAAPA, APAAAAAAAP, APAAAAAAAA, AAPPPPAAAA, AAPPPAAAAP, AAPPPAAAAA, AAPPAPAAAA, AAPPAAAAPP, AAPPAAAAPA, AAPPAAAAAP, AAPPAAAAAA, AAPAPPAAAA, AAPAPAAAAP, AAPAPAAAAA, AAPAAPAAAA, AAPAAAAPPP, AAPAAAAPPA, AAPAAAAPAP, AAPAAAAPAA, AAPAAAAAPP, AAPAAAAAPA, AAPAAAAAAP, AAPAAAAAAA, AAAPPPAAAA, AAAPPAAAAP, AAAPPAAAAA, AAAPAPAAAA, AAAPAAAAPP, AAAPAAAAPA, AAAPAAAAAP, AAAPAAAAAA, AAAAPPPPPP, AAAAPPPPPA, AAAAPPPPAP, AAAAPPPPAA, AAAAPPPAPP, AAAAPPPAPA, AAAAPPPAAP, AAAAPPPAAA, AAAAPPAPPP, AAAAPPAPPA, AAAAPPAPAP, AAAAPPAPAA, AAAAPPAAPP, AAAAPPAAPA, AAAAPPAAAP, AAAAPPAAAA, AAAAPAPPPP, AAAAPAPPPA, AAAAPAPPAP, AAAAPAPPAA, AAAAPAPAPP, AAAAPAPAPA, AAAAPAPAAP, AAAAPAPAAA, AAAAPAAPPP, AAAAPAAPPA, AAAAPAAPAP, AAAAPAAPAA, AAAAPAAAPP, AAAAPAAAPA, AAAAPAAAAP, AAAAPAAAAA, AAAAAPPPPP, AAAAAPPPPA, AAAAAPPPAP, AAAAAPPPAA, AAAAAPPAPP, AAAAAPPAPA, AAAAAPPAAP, AAAAAPPAAA, AAAAAPAPPP, AAAAAPAPPA, AAAAAPAPAP, AAAAAPAPAA, AAAAAPAAPP, AAAAAPAAPA, AAAAAPAAAP, AAAAAPAAAA, AAAAAAPPPP, AAAAAAPPPA, AAAAAAPPAP, AAAAAAPPAA, AAAAAAPAPP, AAAAAAPAPA, AAAAAAPAAP, AAAAAAPAAA, AAAAAAAPPP, AAAAAAAPPA, AAAAAAAPAP, AAAAAAAPAA, AAAAAAAAPP, AAAAAAAAPA, AAAAAAAAAP, AAAAAAAAAA
    count = 251
##### Valid Ways to attend classes over 10 days:
    PPPPPPPPPP, PPPPPPPPPA, PPPPPPPPAP, PPPPPPPPAA, PPPPPPPAPP, PPPPPPPAPA, PPPPPPPAAP, PPPPPPPAAA, PPPPPPAPPP, PPPPPPAPPA, PPPPPPAPAP, PPPPPPAPAA, PPPPPPAAPP, PPPPPPAAPA, PPPPPPAAAP, PPPPPAPPPP, PPPPPAPPPA, PPPPPAPPAP, PPPPPAPPAA, PPPPPAPAPP, PPPPPAPAPA, PPPPPAPAAP, PPPPPAPAAA, PPPPPAAPPP, PPPPPAAPPA, PPPPPAAPAP, PPPPPAAPAA, PPPPPAAAPP, PPPPPAAAPA, PPPPAPPPPP, PPPPAPPPPA, PPPPAPPPAP, PPPPAPPPAA, PPPPAPPAPP, PPPPAPPAPA, PPPPAPPAAP, PPPPAPPAAA, PPPPAPAPPP, PPPPAPAPPA, PPPPAPAPAP, PPPPAPAPAA, PPPPAPAAPP, PPPPAPAAPA, PPPPAPAAAP, PPPPAAPPPP, PPPPAAPPPA, PPPPAAPPAP, PPPPAAPPAA, PPPPAAPAPP, PPPPAAPAPA, PPPPAAPAAP, PPPPAAPAAA, PPPPAAAPPP, PPPPAAAPPA, PPPPAAAPAP, PPPPAAAPAA, PPPAPPPPPP, PPPAPPPPPA, PPPAPPPPAP, PPPAPPPPAA, PPPAPPPAPP, PPPAPPPAPA, PPPAPPPAAP, PPPAPPPAAA, PPPAPPAPPP, PPPAPPAPPA, PPPAPPAPAP, PPPAPPAPAA, PPPAPPAAPP, PPPAPPAAPA, PPPAPPAAAP, PPPAPAPPPP, PPPAPAPPPA, PPPAPAPPAP, PPPAPAPPAA, PPPAPAPAPP, PPPAPAPAPA, PPPAPAPAAP, PPPAPAPAAA, PPPAPAAPPP, PPPAPAAPPA, PPPAPAAPAP, PPPAPAAPAA, PPPAPAAAPP, PPPAPAAAPA, PPPAAPPPPP, PPPAAPPPPA, PPPAAPPPAP, PPPAAPPPAA, PPPAAPPAPP, PPPAAPPAPA, PPPAAPPAAP, PPPAAPPAAA, PPPAAPAPPP, PPPAAPAPPA, PPPAAPAPAP, PPPAAPAPAA, PPPAAPAAPP, PPPAAPAAPA, PPPAAPAAAP, PPPAAAPPPP, PPPAAAPPPA, PPPAAAPPAP, PPPAAAPPAA, PPPAAAPAPP, PPPAAAPAPA, PPPAAAPAAP, PPPAAAPAAA, PPAPPPPPPP, PPAPPPPPPA, PPAPPPPPAP, PPAPPPPPAA, PPAPPPPAPP, PPAPPPPAPA, PPAPPPPAAP, PPAPPPPAAA, PPAPPPAPPP, PPAPPPAPPA, PPAPPPAPAP, PPAPPPAPAA, PPAPPPAAPP, PPAPPPAAPA, PPAPPPAAAP, PPAPPAPPPP, PPAPPAPPPA, PPAPPAPPAP, PPAPPAPPAA, PPAPPAPAPP, PPAPPAPAPA, PPAPPAPAAP, PPAPPAPAAA, PPAPPAAPPP, PPAPPAAPPA, PPAPPAAPAP, PPAPPAAPAA, PPAPPAAAPP, PPAPPAAAPA, PPAPAPPPPP, PPAPAPPPPA, PPAPAPPPAP, PPAPAPPPAA, PPAPAPPAPP, PPAPAPPAPA, PPAPAPPAAP, PPAPAPPAAA, PPAPAPAPPP, PPAPAPAPPA, PPAPAPAPAP, PPAPAPAPAA, PPAPAPAAPP, PPAPAPAAPA, PPAPAPAAAP, PPAPAAPPPP, PPAPAAPPPA, PPAPAAPPAP, PPAPAAPPAA, PPAPAAPAPP, PPAPAAPAPA, PPAPAAPAAP, PPAPAAPAAA, PPAPAAAPPP, PPAPAAAPPA, PPAPAAAPAP, PPAPAAAPAA, PPAAPPPPPP, PPAAPPPPPA, PPAAPPPPAP, PPAAPPPPAA, PPAAPPPAPP, PPAAPPPAPA, PPAAPPPAAP, PPAAPPPAAA, PPAAPPAPPP, PPAAPPAPPA, PPAAPPAPAP, PPAAPPAPAA, PPAAPPAAPP, PPAAPPAAPA, PPAAPPAAAP, PPAAPAPPPP, PPAAPAPPPA, PPAAPAPPAP, PPAAPAPPAA, PPAAPAPAPP, PPAAPAPAPA, PPAAPAPAAP, PPAAPAPAAA, PPAAPAAPPP, PPAAPAAPPA, PPAAPAAPAP, PPAAPAAPAA, PPAAPAAAPP, PPAAPAAAPA, PPAAAPPPPP, PPAAAPPPPA, PPAAAPPPAP, PPAAAPPPAA, PPAAAPPAPP, PPAAAPPAPA, PPAAAPPAAP, PPAAAPPAAA, PPAAAPAPPP, PPAAAPAPPA, PPAAAPAPAP, PPAAAPAPAA, PPAAAPAAPP, PPAAAPAAPA, PPAAAPAAAP, PAPPPPPPPP, PAPPPPPPPA, PAPPPPPPAP, PAPPPPPPAA, PAPPPPPAPP, PAPPPPPAPA, PAPPPPPAAP, PAPPPPPAAA, PAPPPPAPPP, PAPPPPAPPA, PAPPPPAPAP, PAPPPPAPAA, PAPPPPAAPP, PAPPPPAAPA, PAPPPPAAAP, PAPPPAPPPP, PAPPPAPPPA, PAPPPAPPAP, PAPPPAPPAA, PAPPPAPAPP, PAPPPAPAPA, PAPPPAPAAP, PAPPPAPAAA, PAPPPAAPPP, PAPPPAAPPA, PAPPPAAPAP, PAPPPAAPAA, PAPPPAAAPP, PAPPPAAAPA, PAPPAPPPPP, PAPPAPPPPA, PAPPAPPPAP, PAPPAPPPAA, PAPPAPPAPP, PAPPAPPAPA, PAPPAPPAAP, PAPPAPPAAA, PAPPAPAPPP, PAPPAPAPPA, PAPPAPAPAP, PAPPAPAPAA, PAPPAPAAPP, PAPPAPAAPA, PAPPAPAAAP, PAPPAAPPPP, PAPPAAPPPA, PAPPAAPPAP, PAPPAAPPAA, PAPPAAPAPP, PAPPAAPAPA, PAPPAAPAAP, PAPPAAPAAA, PAPPAAAPPP, PAPPAAAPPA, PAPPAAAPAP, PAPPAAAPAA, PAPAPPPPPP, PAPAPPPPPA, PAPAPPPPAP, PAPAPPPPAA, PAPAPPPAPP, PAPAPPPAPA, PAPAPPPAAP, PAPAPPPAAA, PAPAPPAPPP, PAPAPPAPPA, PAPAPPAPAP, PAPAPPAPAA, PAPAPPAAPP, PAPAPPAAPA, PAPAPPAAAP, PAPAPAPPPP, PAPAPAPPPA, PAPAPAPPAP, PAPAPAPPAA, PAPAPAPAPP, PAPAPAPAPA, PAPAPAPAAP, PAPAPAPAAA, PAPAPAAPPP, PAPAPAAPPA, PAPAPAAPAP, PAPAPAAPAA, PAPAPAAAPP, PAPAPAAAPA, PAPAAPPPPP, PAPAAPPPPA, PAPAAPPPAP, PAPAAPPPAA, PAPAAPPAPP, PAPAAPPAPA, PAPAAPPAAP, PAPAAPPAAA, PAPAAPAPPP, PAPAAPAPPA, PAPAAPAPAP, PAPAAPAPAA, PAPAAPAAPP, PAPAAPAAPA, PAPAAPAAAP, PAPAAAPPPP, PAPAAAPPPA, PAPAAAPPAP, PAPAAAPPAA, PAPAAAPAPP, PAPAAAPAPA, PAPAAAPAAP, PAPAAAPAAA, PAAPPPPPPP, PAAPPPPPPA, PAAPPPPPAP, PAAPPPPPAA, PAAPPPPAPP, PAAPPPPAPA, PAAPPPPAAP, PAAPPPPAAA, PAAPPPAPPP, PAAPPPAPPA, PAAPPPAPAP, PAAPPPAPAA, PAAPPPAAPP, PAAPPPAAPA, PAAPPPAAAP, PAAPPAPPPP, PAAPPAPPPA, PAAPPAPPAP, PAAPPAPPAA, PAAPPAPAPP, PAAPPAPAPA, PAAPPAPAAP, PAAPPAPAAA, PAAPPAAPPP, PAAPPAAPPA, PAAPPAAPAP, PAAPPAAPAA, PAAPPAAAPP, PAAPPAAAPA, PAAPAPPPPP, PAAPAPPPPA, PAAPAPPPAP, PAAPAPPPAA, PAAPAPPAPP, PAAPAPPAPA, PAAPAPPAAP, PAAPAPPAAA, PAAPAPAPPP, PAAPAPAPPA, PAAPAPAPAP, PAAPAPAPAA, PAAPAPAAPP, PAAPAPAAPA, PAAPAPAAAP, PAAPAAPPPP, PAAPAAPPPA, PAAPAAPPAP, PAAPAAPPAA, PAAPAAPAPP, PAAPAAPAPA, PAAPAAPAAP, PAAPAAPAAA, PAAPAAAPPP, PAAPAAAPPA, PAAPAAAPAP, PAAPAAAPAA, PAAAPPPPPP, PAAAPPPPPA, PAAAPPPPAP, PAAAPPPPAA, PAAAPPPAPP, PAAAPPPAPA, PAAAPPPAAP, PAAAPPPAAA, PAAAPPAPPP, PAAAPPAPPA, PAAAPPAPAP, PAAAPPAPAA, PAAAPPAAPP, PAAAPPAAPA, PAAAPPAAAP, PAAAPAPPPP, PAAAPAPPPA, PAAAPAPPAP, PAAAPAPPAA, PAAAPAPAPP, PAAAPAPAPA, PAAAPAPAAP, PAAAPAPAAA, PAAAPAAPPP, PAAAPAAPPA, PAAAPAAPAP, PAAAPAAPAA, PAAAPAAAPP, PAAAPAAAPA, APPPPPPPPP, APPPPPPPPA, APPPPPPPAP, APPPPPPPAA, APPPPPPAPP, APPPPPPAPA, APPPPPPAAP, APPPPPPAAA, APPPPPAPPP, APPPPPAPPA, APPPPPAPAP, APPPPPAPAA, APPPPPAAPP, APPPPPAAPA, APPPPPAAAP, APPPPAPPPP, APPPPAPPPA, APPPPAPPAP, APPPPAPPAA, APPPPAPAPP, APPPPAPAPA, APPPPAPAAP, APPPPAPAAA, APPPPAAPPP, APPPPAAPPA, APPPPAAPAP, APPPPAAPAA, APPPPAAAPP, APPPPAAAPA, APPPAPPPPP, APPPAPPPPA, APPPAPPPAP, APPPAPPPAA, APPPAPPAPP, APPPAPPAPA, APPPAPPAAP, APPPAPPAAA, APPPAPAPPP, APPPAPAPPA, APPPAPAPAP, APPPAPAPAA, APPPAPAAPP, APPPAPAAPA, APPPAPAAAP, APPPAAPPPP, APPPAAPPPA, APPPAAPPAP, APPPAAPPAA, APPPAAPAPP, APPPAAPAPA, APPPAAPAAP, APPPAAPAAA, APPPAAAPPP, APPPAAAPPA, APPPAAAPAP, APPPAAAPAA, APPAPPPPPP, APPAPPPPPA, APPAPPPPAP, APPAPPPPAA, APPAPPPAPP, APPAPPPAPA, APPAPPPAAP, APPAPPPAAA, APPAPPAPPP, APPAPPAPPA, APPAPPAPAP, APPAPPAPAA, APPAPPAAPP, APPAPPAAPA, APPAPPAAAP, APPAPAPPPP, APPAPAPPPA, APPAPAPPAP, APPAPAPPAA, APPAPAPAPP, APPAPAPAPA, APPAPAPAAP, APPAPAPAAA, APPAPAAPPP, APPAPAAPPA, APPAPAAPAP, APPAPAAPAA, APPAPAAAPP, APPAPAAAPA, APPAAPPPPP, APPAAPPPPA, APPAAPPPAP, APPAAPPPAA, APPAAPPAPP, APPAAPPAPA, APPAAPPAAP, APPAAPPAAA, APPAAPAPPP, APPAAPAPPA, APPAAPAPAP, APPAAPAPAA, APPAAPAAPP, APPAAPAAPA, APPAAPAAAP, APPAAAPPPP, APPAAAPPPA, APPAAAPPAP, APPAAAPPAA, APPAAAPAPP, APPAAAPAPA, APPAAAPAAP, APPAAAPAAA, APAPPPPPPP, APAPPPPPPA, APAPPPPPAP, APAPPPPPAA, APAPPPPAPP, APAPPPPAPA, APAPPPPAAP, APAPPPPAAA, APAPPPAPPP, APAPPPAPPA, APAPPPAPAP, APAPPPAPAA, APAPPPAAPP, APAPPPAAPA, APAPPPAAAP, APAPPAPPPP, APAPPAPPPA, APAPPAPPAP, APAPPAPPAA, APAPPAPAPP, APAPPAPAPA, APAPPAPAAP, APAPPAPAAA, APAPPAAPPP, APAPPAAPPA, APAPPAAPAP, APAPPAAPAA, APAPPAAAPP, APAPPAAAPA, APAPAPPPPP, APAPAPPPPA, APAPAPPPAP, APAPAPPPAA, APAPAPPAPP, APAPAPPAPA, APAPAPPAAP, APAPAPPAAA, APAPAPAPPP, APAPAPAPPA, APAPAPAPAP, APAPAPAPAA, APAPAPAAPP, APAPAPAAPA, APAPAPAAAP, APAPAAPPPP, APAPAAPPPA, APAPAAPPAP, APAPAAPPAA, APAPAAPAPP, APAPAAPAPA, APAPAAPAAP, APAPAAPAAA, APAPAAAPPP, APAPAAAPPA, APAPAAAPAP, APAPAAAPAA, APAAPPPPPP, APAAPPPPPA, APAAPPPPAP, APAAPPPPAA, APAAPPPAPP, APAAPPPAPA, APAAPPPAAP, APAAPPPAAA, APAAPPAPPP, APAAPPAPPA, APAAPPAPAP, APAAPPAPAA, APAAPPAAPP, APAAPPAAPA, APAAPPAAAP, APAAPAPPPP, APAAPAPPPA, APAAPAPPAP, APAAPAPPAA, APAAPAPAPP, APAAPAPAPA, APAAPAPAAP, APAAPAPAAA, APAAPAAPPP, APAAPAAPPA, APAAPAAPAP, APAAPAAPAA, APAAPAAAPP, APAAPAAAPA, APAAAPPPPP, APAAAPPPPA, APAAAPPPAP, APAAAPPPAA, APAAAPPAPP, APAAAPPAPA, APAAAPPAAP, APAAAPPAAA, APAAAPAPPP, APAAAPAPPA, APAAAPAPAP, APAAAPAPAA, APAAAPAAPP, APAAAPAAPA, APAAAPAAAP, AAPPPPPPPP, AAPPPPPPPA, AAPPPPPPAP, AAPPPPPPAA, AAPPPPPAPP, AAPPPPPAPA, AAPPPPPAAP, AAPPPPPAAA, AAPPPPAPPP, AAPPPPAPPA, AAPPPPAPAP, AAPPPPAPAA, AAPPPPAAPP, AAPPPPAAPA, AAPPPPAAAP, AAPPPAPPPP, AAPPPAPPPA, AAPPPAPPAP, AAPPPAPPAA, AAPPPAPAPP, AAPPPAPAPA, AAPPPAPAAP, AAPPPAPAAA, AAPPPAAPPP, AAPPPAAPPA, AAPPPAAPAP, AAPPPAAPAA, AAPPPAAAPP, AAPPPAAAPA, AAPPAPPPPP, AAPPAPPPPA, AAPPAPPPAP, AAPPAPPPAA, AAPPAPPAPP, AAPPAPPAPA, AAPPAPPAAP, AAPPAPPAAA, AAPPAPAPPP, AAPPAPAPPA, AAPPAPAPAP, AAPPAPAPAA, AAPPAPAAPP, AAPPAPAAPA, AAPPAPAAAP, AAPPAAPPPP, AAPPAAPPPA, AAPPAAPPAP, AAPPAAPPAA, AAPPAAPAPP, AAPPAAPAPA, AAPPAAPAAP, AAPPAAPAAA, AAPPAAAPPP, AAPPAAAPPA, AAPPAAAPAP, AAPPAAAPAA, AAPAPPPPPP, AAPAPPPPPA, AAPAPPPPAP, AAPAPPPPAA, AAPAPPPAPP, AAPAPPPAPA, AAPAPPPAAP, AAPAPPPAAA, AAPAPPAPPP, AAPAPPAPPA, AAPAPPAPAP, AAPAPPAPAA, AAPAPPAAPP, AAPAPPAAPA, AAPAPPAAAP, AAPAPAPPPP, AAPAPAPPPA, AAPAPAPPAP, AAPAPAPPAA, AAPAPAPAPP, AAPAPAPAPA, AAPAPAPAAP, AAPAPAPAAA, AAPAPAAPPP, AAPAPAAPPA, AAPAPAAPAP, AAPAPAAPAA, AAPAPAAAPP, AAPAPAAAPA, AAPAAPPPPP, AAPAAPPPPA, AAPAAPPPAP, AAPAAPPPAA, AAPAAPPAPP, AAPAAPPAPA, AAPAAPPAAP, AAPAAPPAAA, AAPAAPAPPP, AAPAAPAPPA, AAPAAPAPAP, AAPAAPAPAA, AAPAAPAAPP, AAPAAPAAPA, AAPAAPAAAP, AAPAAAPPPP, AAPAAAPPPA, AAPAAAPPAP, AAPAAAPPAA, AAPAAAPAPP, AAPAAAPAPA, AAPAAAPAAP, AAPAAAPAAA, AAAPPPPPPP, AAAPPPPPPA, AAAPPPPPAP, AAAPPPPPAA, AAAPPPPAPP, AAAPPPPAPA, AAAPPPPAAP, AAAPPPPAAA, AAAPPPAPPP, AAAPPPAPPA, AAAPPPAPAP, AAAPPPAPAA, AAAPPPAAPP, AAAPPPAAPA, AAAPPPAAAP, AAAPPAPPPP, AAAPPAPPPA, AAAPPAPPAP, AAAPPAPPAA, AAAPPAPAPP, AAAPPAPAPA, AAAPPAPAAP, AAAPPAPAAA, AAAPPAAPPP, AAAPPAAPPA, AAAPPAAPAP, AAAPPAAPAA, AAAPPAAAPP, AAAPPAAAPA, AAAPAPPPPP, AAAPAPPPPA, AAAPAPPPAP, AAAPAPPPAA, AAAPAPPAPP, AAAPAPPAPA, AAAPAPPAAP, AAAPAPPAAA, AAAPAPAPPP, AAAPAPAPPA, AAAPAPAPAP, AAAPAPAPAA, AAAPAPAAPP, AAAPAPAAPA, AAAPAPAAAP, AAAPAAPPPP, AAAPAAPPPA, AAAPAAPPAP, AAAPAAPPAA, AAAPAAPAPP, AAAPAAPAPA, AAAPAAPAAP, AAAPAAPAAA, AAAPAAAPPP, AAAPAAAPPA, AAAPAAAPAP, AAAPAAAPAA
    count = 773
##### Ways in which the graduation ceremony will be missed i.e. Class is missed on last day:
    PPPPPPPPPA, PPPPPPPPAA, PPPPPPPAPA, PPPPPPPAAA, PPPPPPAPPA, PPPPPPAPAA, PPPPPPAAPA, PPPPPAPPPA, PPPPPAPPAA, PPPPPAPAPA, PPPPPAPAAA, PPPPPAAPPA, PPPPPAAPAA, PPPPPAAAPA, PPPPAPPPPA, PPPPAPPPAA, PPPPAPPAPA, PPPPAPPAAA, PPPPAPAPPA, PPPPAPAPAA, PPPPAPAAPA, PPPPAAPPPA, PPPPAAPPAA, PPPPAAPAPA, PPPPAAPAAA, PPPPAAAPPA, PPPPAAAPAA, PPPAPPPPPA, PPPAPPPPAA, PPPAPPPAPA, PPPAPPPAAA, PPPAPPAPPA, PPPAPPAPAA, PPPAPPAAPA, PPPAPAPPPA, PPPAPAPPAA, PPPAPAPAPA, PPPAPAPAAA, PPPAPAAPPA, PPPAPAAPAA, PPPAPAAAPA, PPPAAPPPPA, PPPAAPPPAA, PPPAAPPAPA, PPPAAPPAAA, PPPAAPAPPA, PPPAAPAPAA, PPPAAPAAPA, PPPAAAPPPA, PPPAAAPPAA, PPPAAAPAPA, PPPAAAPAAA, PPAPPPPPPA, PPAPPPPPAA, PPAPPPPAPA, PPAPPPPAAA, PPAPPPAPPA, PPAPPPAPAA, PPAPPPAAPA, PPAPPAPPPA, PPAPPAPPAA, PPAPPAPAPA, PPAPPAPAAA, PPAPPAAPPA, PPAPPAAPAA, PPAPPAAAPA, PPAPAPPPPA, PPAPAPPPAA, PPAPAPPAPA, PPAPAPPAAA, PPAPAPAPPA, PPAPAPAPAA, PPAPAPAAPA, PPAPAAPPPA, PPAPAAPPAA, PPAPAAPAPA, PPAPAAPAAA, PPAPAAAPPA, PPAPAAAPAA, PPAAPPPPPA, PPAAPPPPAA, PPAAPPPAPA, PPAAPPPAAA, PPAAPPAPPA, PPAAPPAPAA, PPAAPPAAPA, PPAAPAPPPA, PPAAPAPPAA, PPAAPAPAPA, PPAAPAPAAA, PPAAPAAPPA, PPAAPAAPAA, PPAAPAAAPA, PPAAAPPPPA, PPAAAPPPAA, PPAAAPPAPA, PPAAAPPAAA, PPAAAPAPPA, PPAAAPAPAA, PPAAAPAAPA, PAPPPPPPPA, PAPPPPPPAA, PAPPPPPAPA, PAPPPPPAAA, PAPPPPAPPA, PAPPPPAPAA, PAPPPPAAPA, PAPPPAPPPA, PAPPPAPPAA, PAPPPAPAPA, PAPPPAPAAA, PAPPPAAPPA, PAPPPAAPAA, PAPPPAAAPA, PAPPAPPPPA, PAPPAPPPAA, PAPPAPPAPA, PAPPAPPAAA, PAPPAPAPPA, PAPPAPAPAA, PAPPAPAAPA, PAPPAAPPPA, PAPPAAPPAA, PAPPAAPAPA, PAPPAAPAAA, PAPPAAAPPA, PAPPAAAPAA, PAPAPPPPPA, PAPAPPPPAA, PAPAPPPAPA, PAPAPPPAAA, PAPAPPAPPA, PAPAPPAPAA, PAPAPPAAPA, PAPAPAPPPA, PAPAPAPPAA, PAPAPAPAPA, PAPAPAPAAA, PAPAPAAPPA, PAPAPAAPAA, PAPAPAAAPA, PAPAAPPPPA, PAPAAPPPAA, PAPAAPPAPA, PAPAAPPAAA, PAPAAPAPPA, PAPAAPAPAA, PAPAAPAAPA, PAPAAAPPPA, PAPAAAPPAA, PAPAAAPAPA, PAPAAAPAAA, PAAPPPPPPA, PAAPPPPPAA, PAAPPPPAPA, PAAPPPPAAA, PAAPPPAPPA, PAAPPPAPAA, PAAPPPAAPA, PAAPPAPPPA, PAAPPAPPAA, PAAPPAPAPA, PAAPPAPAAA, PAAPPAAPPA, PAAPPAAPAA, PAAPPAAAPA, PAAPAPPPPA, PAAPAPPPAA, PAAPAPPAPA, PAAPAPPAAA, PAAPAPAPPA, PAAPAPAPAA, PAAPAPAAPA, PAAPAAPPPA, PAAPAAPPAA, PAAPAAPAPA, PAAPAAPAAA, PAAPAAAPPA, PAAPAAAPAA, PAAAPPPPPA, PAAAPPPPAA, PAAAPPPAPA, PAAAPPPAAA, PAAAPPAPPA, PAAAPPAPAA, PAAAPPAAPA, PAAAPAPPPA, PAAAPAPPAA, PAAAPAPAPA, PAAAPAPAAA, PAAAPAAPPA, PAAAPAAPAA, PAAAPAAAPA, APPPPPPPPA, APPPPPPPAA, APPPPPPAPA, APPPPPPAAA, APPPPPAPPA, APPPPPAPAA, APPPPPAAPA, APPPPAPPPA, APPPPAPPAA, APPPPAPAPA, APPPPAPAAA, APPPPAAPPA, APPPPAAPAA, APPPPAAAPA, APPPAPPPPA, APPPAPPPAA, APPPAPPAPA, APPPAPPAAA, APPPAPAPPA, APPPAPAPAA, APPPAPAAPA, APPPAAPPPA, APPPAAPPAA, APPPAAPAPA, APPPAAPAAA, APPPAAAPPA, APPPAAAPAA, APPAPPPPPA, APPAPPPPAA, APPAPPPAPA, APPAPPPAAA, APPAPPAPPA, APPAPPAPAA, APPAPPAAPA, APPAPAPPPA, APPAPAPPAA, APPAPAPAPA, APPAPAPAAA, APPAPAAPPA, APPAPAAPAA, APPAPAAAPA, APPAAPPPPA, APPAAPPPAA, APPAAPPAPA, APPAAPPAAA, APPAAPAPPA, APPAAPAPAA, APPAAPAAPA, APPAAAPPPA, APPAAAPPAA, APPAAAPAPA, APPAAAPAAA, APAPPPPPPA, APAPPPPPAA, APAPPPPAPA, APAPPPPAAA, APAPPPAPPA, APAPPPAPAA, APAPPPAAPA, APAPPAPPPA, APAPPAPPAA, APAPPAPAPA, APAPPAPAAA, APAPPAAPPA, APAPPAAPAA, APAPPAAAPA, APAPAPPPPA, APAPAPPPAA, APAPAPPAPA, APAPAPPAAA, APAPAPAPPA, APAPAPAPAA, APAPAPAAPA, APAPAAPPPA, APAPAAPPAA, APAPAAPAPA, APAPAAPAAA, APAPAAAPPA, APAPAAAPAA, APAAPPPPPA, APAAPPPPAA, APAAPPPAPA, APAAPPPAAA, APAAPPAPPA, APAAPPAPAA, APAAPPAAPA, APAAPAPPPA, APAAPAPPAA, APAAPAPAPA, APAAPAPAAA, APAAPAAPPA, APAAPAAPAA, APAAPAAAPA, APAAAPPPPA, APAAAPPPAA, APAAAPPAPA, APAAAPPAAA, APAAAPAPPA, APAAAPAPAA, APAAAPAAPA, AAPPPPPPPA, AAPPPPPPAA, AAPPPPPAPA, AAPPPPPAAA, AAPPPPAPPA, AAPPPPAPAA, AAPPPPAAPA, AAPPPAPPPA, AAPPPAPPAA, AAPPPAPAPA, AAPPPAPAAA, AAPPPAAPPA, AAPPPAAPAA, AAPPPAAAPA, AAPPAPPPPA, AAPPAPPPAA, AAPPAPPAPA, AAPPAPPAAA, AAPPAPAPPA, AAPPAPAPAA, AAPPAPAAPA, AAPPAAPPPA, AAPPAAPPAA, AAPPAAPAPA, AAPPAAPAAA, AAPPAAAPPA, AAPPAAAPAA, AAPAPPPPPA, AAPAPPPPAA, AAPAPPPAPA, AAPAPPPAAA, AAPAPPAPPA, AAPAPPAPAA, AAPAPPAAPA, AAPAPAPPPA, AAPAPAPPAA, AAPAPAPAPA, AAPAPAPAAA, AAPAPAAPPA, AAPAPAAPAA, AAPAPAAAPA, AAPAAPPPPA, AAPAAPPPAA, AAPAAPPAPA, AAPAAPPAAA, AAPAAPAPPA, AAPAAPAPAA, AAPAAPAAPA, AAPAAAPPPA, AAPAAAPPAA, AAPAAAPAPA, AAPAAAPAAA, AAAPPPPPPA, AAAPPPPPAA, AAAPPPPAPA, AAAPPPPAAA, AAAPPPAPPA, AAAPPPAPAA, AAAPPPAAPA, AAAPPAPPPA, AAAPPAPPAA, AAAPPAPAPA, AAAPPAPAAA, AAAPPAAPPA, AAAPPAAPAA, AAAPPAAAPA, AAAPAPPPPA, AAAPAPPPAA, AAAPAPPAPA, AAAPAPPAAA, AAAPAPAPPA, AAAPAPAPAA, AAAPAPAAPA, AAAPAAPPPA, AAAPAAPPAA, AAAPAAPAPA, AAAPAAPAAA, AAAPAAAPPA, AAAPAAAPAA
    count = 372

Therefore, Answer of (1) = 773 , Answer of (2) = 372/773

# How to Run the program

**Prerequisite**: Python 3 must be installed in your local machine.

To run the assignment execute following command:

```
python3 main.py 5
```

Here 5 is the number of days, value for N.