# File to Generate Web Page to Run the code
# To Run use the following in cmd
# python -m streamlit run c:\path\main.py

import os

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

def AI_function(inp_str):
    print("This is AI Function")
    print(inp_str)
    return "Output From AI Function" + inp_str

steps=['Characters',
       'Story',
       'Game Universe',
       'Anything Else']

# App framework
st.title('� �️ World Builder LLC �️  �')



# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
#llm = OpenAI(temperature=0.9)
#title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
#script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

#wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt

base_idea = st.text_input('What is your Game Idea ? ')
game_inp = []
if base_idea:
    #title = title_chain.run(prompt)
    #wiki_research = wiki.run(prompt)
    #script = script_chain.run(title=title, wikipedia_research=wiki_research)

    #st.write(title)
    #st.write(script)

    #with st.expander('Title History'):
    #    st.info(title_memory.buffer)

    #with st.expander('Script History'):
    #    st.info(script_memory.buffer)

    #with st.expander('Wikipedia Research'):
    #    st.info(wiki_research)
    steps = ['Characters',
             'Story',
             'Game Universe',
             'Anything Else']


    _characters = st.text_input('Do you have an idea about '+steps[0] + ' ?')
    if _characters:
        game_inp.append(_characters)
        _story = st.text_input('Do you have an idea about ' + steps[1] + ' ?')
        if _story:
            game_inp.append(_story)
            _univ = st.text_input('Do you have an idea about ' + steps[2] + ' ?')
            if _univ:
                game_inp.append(_univ)
                _extra = st.text_input('Do you want to take not of ' + steps[3] + ' ?')
                if _extra:
                    game_inp.append(_extra)

if base_idea and _characters and _story and _univ and _extra:
    st.write(AI_function("We are creating game with idea of " + base_idea))

    for cur_attr in game_inp:
        st.write(AI_function(" The attribute to pass to LLM is " + cur_attr))

    st.write("LETS GENERATE the AI game story for you")
