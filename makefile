all: data.dat movie.png

%.png: %.dat movie.png
	python3 graficar.py
	
%.dat: a.out
	./a.out

a.out: JuanVelasquez_Ejercicio30.cpp
	g++ JuanVelasquez_Ejercicio30.cpp

clean:
	rm -rf *.x *.dat *.png