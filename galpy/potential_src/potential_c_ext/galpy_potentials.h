/* C implementations of galpy potentials */
/*
  Function declarations
*/
//ZeroForce
double ZeroPlanarForce(double, double,double,int, double *);
double ZeroForce(double,double,double,double,int, double *);
//LogarithmicHaloPotential
double LogarithmicHaloPotentialRforce(double ,double , double, double,
				      int , double *);
double LogarithmicHaloPotentialPlanarRforce(double ,double, double,
					    int , double *);
double LogarithmicHaloPotentialzforce(double,double,double,double,
				      int, double *);
double LogarithmicHaloPotentialPlanarR2deriv(double ,double, double,
					     int , double *);
//DehnenBarPotential
double DehnenBarPotentialRforce(double,double,double,int,double *);
double DehnenBarPotentialphiforce(double,double,double,int,double *);
double DehnenBarPotentialR2deriv(double,double,double,int,double *);
double DehnenBarPotentialphi2deriv(double,double,double,int,double *);
double DehnenBarPotentialRphideriv(double,double,double,int,double *);
//TransientLogSpiralPotential
double TransientLogSpiralPotentialRforce(double,double,double,int,double *);
double TransientLogSpiralPotentialphiforce(double,double,double,int,double *);
//SteadyLogSpiralPotential
double SteadyLogSpiralPotentialRforce(double,double,double,int,double *);
double SteadyLogSpiralPotentialphiforce(double,double,double,int,double *);
//EllipticalDiskPotential
double EllipticalDiskPotentialRforce(double,double,double,int,double *);
double EllipticalDiskPotentialphiforce(double,double,double,int,double *);
double EllipticalDiskPotentialR2deriv(double,double,double,int,double *);
double EllipticalDiskPotentialphi2deriv(double,double,double,int,double *);
double EllipticalDiskPotentialRphideriv(double,double,double,int,double *);
//Miyamoto-Nagai Potential
double MiyamotoNagaiPotentialRforce(double ,double , double, double,
				    int , double *);
double MiyamotoNagaiPotentialPlanarRforce(double ,double, double,
					  int , double *);
double MiyamotoNagaiPotentialzforce(double,double,double,double,
				    int, double *);
double MiyamotoNagaiPotentialPlanarR2deriv(double ,double, double,
					   int , double *);
//LopsidedDiskPotential
double LopsidedDiskPotentialRforce(double,double,double,int,double *);
double LopsidedDiskPotentialphiforce(double,double,double,int,double *);
double LopsidedDiskPotentialR2deriv(double,double,double,int,double *);
double LopsidedDiskPotentialphi2deriv(double,double,double,int,double *);
double LopsidedDiskPotentialRphideriv(double,double,double,int,double *);
//PowerSphericalPotential
double PowerSphericalPotentialRforce(double ,double , double, double,
				     int , double *);
double PowerSphericalPotentialPlanarRforce(double ,double, double,
					   int , double *);
double PowerSphericalPotentialzforce(double,double,double,double,
				     int, double *);
double PowerSphericalPotentialPlanarR2deriv(double ,double, double,
					    int , double *);
