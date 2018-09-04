// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

//创建节点结构
typedef struct node
{
	char word[LENGTH + 1];
	//在node结构中创建一个名叫next的指针
	struct node *next;
}
node;

//创建指向node结构的指针
node *thedict = NULL;
char wordtmp[LENGTH + 1];

// Returns true if word is in dictionary else 0
bool check(const char *word)
{
	//字典中寻找相同hash值的字符串
	//创建一个指针，指向hash字典
	for (node *cursor = thedict; cursor != NULL; cursor = cursor->next)
	{
		if (strcasecmp(word,cursor->word))
		{
			return 1;
		}
	}
	return 0;
}

// Loads dictionary into memory, returning 1 if successful else 0
bool load(const char *dictionary)
{
	//打开字典，一行一行读取字典里面的词
	FILE *inptr = fopen(dictionary,"r");
	if (inptr == NULL) 
	{
		fprintf(stderr,"Could not open dictionary.\n");
		return 0;
	}
	while (fscanf(inptr, "%s", wordtmp) != EOF)
	{
		//分配空间
		node *new = malloc(sizeof(node));
    	if (!new)
    	{
    		fprintf(stderr,"Could not allocate memory for node.\n");
    		unload();
    		return 0;
    	} 
    	//添加字典里面的词,用strcpy，不然随着tmp更新，每个node都会变成一样
    	strcpy(new->word,wordtmp);
    	new->next = NULL;
    	//字典有词的话就找到最后一个，添加
    	//可以尝试直接在最前面添加
    	if (thedict)
		{
			for (node *ptr = thedict;ptr != NULL; ptr = ptr->next)
    		{
    			if (ptr->next == NULL)
    			{
    				ptr->next = new;
    			}
    		}
		}
    	else
    	{
    		thedict = new;
    	}
	}
	return 1;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning 1 if successful else 0
bool unload(void)
{
	for (node *cursor = thedict; cursor != NULL; cursor = cursor->next)
	{
		node *temp = cursor;
		cursor = cursor->next;
		free(temp);
	}
	return 1;
}