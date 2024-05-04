# La séquence de fin de ligne dans le fichier input.1 peut différer selon le système d'exploitation
# nottament entre Ubuntu et WSL ou MacOS. Cela peut causer une erreur de syntaxe lors de l'analyse
# du fichier, pour résoudre ce problème, installer dos2unix avec la commande make install (retirer
# le # dans install et dans regexp) puis run le programme avec make.

run: main.py
	python3 main.py

main.py: regexp input.1
	./regexp < input.1

regexp: regexp.yy.c regexp.tab.c
	gcc -o $@ $^ -ly -ll
#	gcc -mmacosx-version-min=13.1 -o $@ $^ ${"-L/usr/local/opt/flex/lib"} -ly -lfl
#	dos2unix input.1

regexp.tab.c: regexp.y
	bison -d --report=all $^

regexp.yy.c: regexp.l
	flex -o $@ $^

install:
	sudo apt-get install -y libbison-dev
#	sudo apt-get install dos2unix

clean:
	rm -f regexp.yy.c   rm -f regexp.output regexp.tab.c regexp.tab.h
	rm -f regexp
	rm -rf __pycache__
	ls -als
	truncate -c -s 0 main.py