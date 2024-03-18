run: main.py
	python3 main.py

main.py: regexp input.1
	./regexp < input.1

regexp: regexp.yy.c regexp.tab.c
	gcc -o $@ $^ -ly -ll
#	gcc -mmacosx-version-min=13.1 -o $@ $^ ${"-L/usr/local/opt/flex/lib"} -ly -lfl

regexp.tab.c: regexp.y
	bison -d --report=all $^

regexp.yy.c: regexp.l
	flex -o $@ $^

install:
	sudo apt-get install -y libbison-dev

clean:
	rm -f regexp.yy.c   rm -f regexp.output regexp.tab.c regexp.tab.h
	rm -f regexp
	ls -als
	truncate -c -s 0 main.py