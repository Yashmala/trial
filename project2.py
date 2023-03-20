# word counter project which counts the words in large amount of text,speech but not the characters

# so we will firstly take a large text
#triple quotes can also be used to add multline string but if we pass this into string variable 
# it wouldn't be counted as comments  
text1=""" Find in transcript ,Filter results by video selectedIn this video Splitting a string
Selecting transcript lines in this section will navigate to timestamp in the video. Congratulations. You've learned enough Python to bring on yet another project.
This project is going to be the word counter. The idea is that we can take a really large piece of text,
maybe a speech, a song, a whole book even, and we can say this is how many words there are in this piece of text
and this is how often this word appears or this word or this word. So before we move forward,
there's one last concept that we'vpart, in the middle, I can put this whole Gettysburg Address and this is just one big string. If you're using song lyrics, this will 
be really helpful because there's just tons and tons of new lines that you would have to deal with. So just 
to make sure this is working, let's go ahead and print out the text here. Make sure that our triple quote is all
that we thought it was. We'll hit Run and we can see The Gettysburg Address is printing. Now here's that 
situation. et and then we have an ending square bracket and we now have a list of a bunch of strings. So what we could do now is say, okay, I want to know the length of this list of words. So if we go ahead and run this, now we can see that we have 278 words.
So this is probably a good place for us to stop. We've learned how to take really big strings and represent"""
print(len(text1))#so length will give the no. of characters
print(text1.split())# tis will form the list of splitted words
print(len(text1.split()))# this will split the words acc.to ending space and stating spaces and thus we counts the splitted words




## repeated word counter 
word_count={} 
for word in text1.split():
    if word in word_count: # when we get word we will increment the value,thus the key is word but the vice vers cannot be done
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)
dictionary1=word_count.values()
print(dictionary1)
print(max(dictionary1))