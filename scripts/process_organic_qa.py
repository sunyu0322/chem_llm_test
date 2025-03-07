import os
import re
import csv
from langchain_openai import ChatOpenAI

# 直接集成的模型配置
BASE_URL = "https://api.fe8.cn/v1"
API_KEY = "sk-bsFsOAvTdyNI2MD25vcLXID1vJaYM1hEsN1HMZSuygvXjgiZ"

def generate_answer_from_gpt_4o(query: str) -> str:
    """直接内嵌的模型调用函数"""
    try:
        model = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            base_url=BASE_URL,
            api_key=API_KEY
        )
        response = model.invoke(f'''
        你是一个化学教材解析专家，需要从Markdown内容中提取所有问题对：
        1. 识别所有以"problem"或"question"开头的内容作为问题
        2. 对应的"suggested solution"或"answer"作为答案
        3. 保留所有SMILES代码（格式如`[O]C`）
        4. 按严格CSV格式返回：
           question,answer
           "问题内容","答案内容"
           ...
        以下是需要处理的内容：
        {query}
        ''')
        return response.content.strip()
    
    except Exception as e:
        print(f"模型调用失败: {e}")
        return ""

print(generate_answer_from_gpt_4o(
    '''

## Suggested solutions for Chapter 2

## Problem 1

Draw good diagrams of saturated hydrocarbons with seven carbon atoms having (a) mean, (b) branched, and (c) tycks frameworks. Draw molecules based on each framework having both ketone and carboxylic adic functional groups.

## Purpose of the problem

To get you drawing simple structures well and to steer you away from rules and names towards creative structural ideas.

## Suggested solution

There is only one linear saturated hydrocarbon with seven carbon atoms but there is a wide choice for the rest. We offer some possibilities but you may well have thought of others.

<!-- Media -->

<!-- figureText: linear saturated hydrocarbon (complexe) series instituting constants. same cycle hydrocarbons -->

`CC1CCCCCC1.CC1CCCCC1.CC1CCCC1.CC1CCCC1.CC1(C)CCCC1.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C.CCCCC(C)C`

<!-- Media -->

We give just a few examples for the ketones and carboxylic acids. You will notice that no Cr carbocyclic acid is possible based on, say, cycloheptane without adding an extra carbon atom.
## Problem 2

<!-- Media -->

<!-- figureText: linear ketone and carbonyle sold branched isotone and carboxylic cold cyclic lations and carbonylic and -->

`CCC(C)(C)C(=O)C.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CCCCCCC(=O)O.CC1CCCC1C(=O)O.C1CCCC(CC1)C(=O)O.C1CCCC(C1)C(=O)O.C1CCC(C1)C(=O)O.C1CCC(C1)C(=O)O`

<!-- Media -->

Study the structure of brevelosis on a. 33. Make a list of the different types of functional group (you already know that there are many effect and of the numbers of range of different states. Finally, study the carbon framework - is in linear, cyclic, or branched?

## Purpose of the problem

To persuade you that functional groups are easily recognized even in complicated molecules and that, say, an ester is an ester whatever company it may keep. You were not expected to see the full implications of the carbon framework part of the question. That was to amuse and surprise you.

## Suggested solution

The ethers are all the unmarked oxygen atoms in the rings: all are cyclic, seven in six-membered rings, two in seven-membered rings, and one in an eight-membered ring. There are two carbonyl groups, one an ester and one an aldehyde, and three alkenes.

<!-- Media -->

`CC(C)C1=CC(=O)O[C@@]2(C)C[C@@]3(C)[C@@](C)(C[C@@]4(C)[C@@](C)(C[C@@H]([C@@]5(C)[C@@](C)(CC[C@@]6(C)[C@@](C)(C[C@@]7(C)[C@@](C)(C[C@@H]([C@@]8(C)[C@@](C)(C[C@@]9(C)[C@@](C)(C[C@@]%10(C)[C@@](C)(C[C@@H](C[C@@H](CC(=O)C(C)(C)OC=O)O%10)O9)O8)O7)O6)OC)O5)O4)O3)OC=O)O2)O1`

<!-- Media -->

The carbon chain is branched because it has seven methyl groups branching off it and the aldehyde is also a branch. Amazingly, under this disguise, you can detect a basically linear carbon chain, shown with a thick black line, although it twists and turns throughout the entire molecule! 

## Problem 3

<!-- Media -->

`C=C(C[C@@H]1C[C@@H]([C@@]2([C@](C)(C[C@]3([C@@](C)(C[C@]4([C@@](C)(C=CC[C@@]5([C@@](C)(C[C@]6([C@@](C)(C[C@]7([C@@](C)(CC[C@@]8([C@@](C)(C[C@@]9([C@@](C)(C[C@@]%10([C@@](C)(C[C@@]%11(C)[C@@](C)(C(=CC(=O)O%11)N)O%10)O9)O8)O7)O6)O5)O)O4)O)O3)O2)O)O1)O)O)O)O)O)O)O`

<!-- Media -->

What is wrong with these structures? Suggest better ways of representing these molecules.

<!-- Media -->

`C1=CC=CC=C1.C#CC(C#C[Hg])(O)[R19a].C1CN(C1)[Z]([H])([H])NC(=O)[Z]([H])([H])[H].C.C.N`

<!-- Media -->

## Purpose of the problem

To shock you with two dreadful structures and to try and convince you that well drawn realistic structures are more attractive to the eye as well as easier to understand.

## Suggested solution

The bond angles are grotesque with square planar saturated carbon,alkynes at \( {120}^{ \circ  } \) ,alkenes at \( {180}^{ \circ  } \) , bonds coming off benzene rings at the wrong angle, and so on. The left-hand structure would be clearer if most of the hydrogens were omitted. Here are two possible better structures for each molecule. There are many other correct possibilities.

<!-- Media -->

`CC#CC(/C=C/C1=CC=C(C=C1)N)O.CC#CC(/C=C/C1=CC=C(C=C1)N)O.CC(=O)NCN1CCCC1.CC(=O)NCN1CCCC1`

<!-- Media -->

## Problem 4

Draw structures corresponding to these names. In each case suggest alternative names that might convey the structure more clearly to someone who is listening to you speak.

(a) 1,4-di-(1,1-dimethylethyl)benzene

(b) 3-(prop-2-enyloxy)prop-1-ene

(c) cyclohexa-1,3,5-triene

## Purpose of the problem

To help you appreciate the limitations of names, the usefulness of names for part structures, and, in the case of (c), to amuse.

## Suggested solution

(a) 1,4-di-(1,1-dimethylethyl)benzene. More helpful name para-di-t-butyl benzene. It is sold as 1,4-di-tert-butyl benzene, an equally helpful name.

<!-- Media -->

<!-- figureText: the 1,1-dimethylethyl group 1,4 relationship between the two substituents on the benzene ring -->

`CC(C)(C)C1=CC=C(C=C1)C(C)(C)C.CC(C)(C)C1=CC=CC=C1.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC(C)(C)C.CC`

<!-- Media -->

(b) 3-( prop-2-enyloxy)prop-1-ene. This name does not convey the simple symmetrical structure nor that it contains two allyl groups. Most chemists would call this 'diallyl ether' though it is sold as 'allyl ether'.

<!-- Media -->

`CC1=CC2=C(C=C1)N=C(C3=CC4=C(C=C3)N=C(C5=CC=CC=C5)N4)N2.CC1=CC2=C(C=C1)N=C(C3=CC=CC=C3)N2.CC1=CC2=C(C=C1)N=C(C3=CC=CC=C3)N2.CC1=CC2=C(C=C1)N=C(C3=CC=CC=C3)N2`

<!-- Media -->

(c) cyclohexa-1,3,5-triene. This is, of course, benzene, but even IUPAC has not tried to impose this 'correct' name for such an important compound.
'''
))