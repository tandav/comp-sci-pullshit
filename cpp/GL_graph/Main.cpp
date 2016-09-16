#include <gl/glut.h>
#include <math.h>

float WinWid = 640;//Ширина окна
float WinHei = 640;//Высота окна
float X = 0, Y = 0, t = -30, phi = -30, r, a;



void Draw()
{
	
	glClear(GL_COLOR_BUFFER_BIT);

	glBegin(GL_POINTS);
	glVertex2f(phi, sin(phi) / phi);
	glEnd();


	// glBegin(GL_LINE_LOOP);
	// glVertex2f(0 - 5, 0);
	// glVertex2f(0 + 5, 0);
	// glVertex2f(0 + 5, 5);
	// glVertex2f(0 - 5, 5);
	// glEnd();
	



	glutSwapBuffers();
}


void Timer(int=0)
{
	phi += 0.001;
	a = 10;
	r = 40/(1-0.9*cos(phi));
	//if (t > 70) return;
	//t+=0.1;
	Draw();
	glutTimerFunc(0.001, Timer, 0);
}

void Initialize()
{
	glClearColor(0.8, 0.3, 0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-30, 30, -10, 7, -200.0, 200.0);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(WinWid, WinHei);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("y = sin(x) / x");
	glutDisplayFunc(Draw);
	Timer();

	Initialize();
	glutMainLoop();
	return 0;
}