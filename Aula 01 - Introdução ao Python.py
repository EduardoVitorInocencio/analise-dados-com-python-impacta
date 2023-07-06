#!/usr/bin/env python
# coding: utf-8

# # Aula 1
# 
# ###### Introdução ao Python
# 
# Para declarar uma variável, basta escrever o nome da variável e inserir o sinal de igual antes do valor.
# 

# In[6]:


fruta = "banana"


# ###### Para Acessar o valor guardado, basta chamar novamente a variável
# 

# In[7]:


fruta


# In[12]:


x = 10
x


# ## Função type()
# A função type() retorna o tipo do objeto ou retorna um novo tipo de objeto com base nos argumentos passados

# In[15]:


type (x)


# In[17]:


x = x/2


# In[18]:


x


# In[19]:


type (x)


# #### Atribuindo Múltiplas Variáveis

# In[24]:


x, y, z = 1,2,3


# In[25]:


x


# In[26]:


y


# In[27]:


z


# In[30]:


print(type(x))

x = float(x)

print(type(x))


# In[ ]:


x

