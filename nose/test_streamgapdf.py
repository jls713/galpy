import numpy

# Test the routine that rotates vectors to an arbitrary vector
def test_rotate_to_arbitrary_vector():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,1.,0])
    assert numpy.fabs(ma[0,0,1]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,0,1.])
    assert numpy.fabs(ma[0,0,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # Rotate to same should be unit matrix
    ma= streamgapdf._rotate_to_arbitrary_vector(v,v[0])
    assert numpy.all(numpy.fabs(numpy.diag(ma[0])-1.) < 10.**tol), \
        'Rotation matrix to same vector is not unity'
    assert numpy.fabs(numpy.sum(ma**2.)-3.)< 10.**tol, \
        'Rotation matrix to same vector is not unity'
    # Rotate to -same should be -unit matrix
    ma= streamgapdf._rotate_to_arbitrary_vector(v,-v[0])
    assert numpy.all(numpy.fabs(numpy.diag(ma[0])+1.) < 10.**tol), \
        'Rotation matrix to minus same vector is not minus unity'
    assert numpy.fabs(numpy.sum(ma**2.)-3.)< 10.**tol, \
        'Rotation matrix to minus same vector is not minus unity'
    return None

# Test that the rotation routine works for multiple vectors
def test_rotate_to_arbitrary_vector_multi():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.],[0.,1.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotate_to_arbitrary_vector(v,[0,0,1.])
    assert numpy.fabs(ma[0,0,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    # 2nd
    assert numpy.fabs(ma[1,1,2]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,1]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,1,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[1,2,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    return None

# Test the inverse of the routine that rotates vectors to an arbitrary vector
def test_rotate_to_arbitrary_vector_inverse():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to random vector and back
    a= numpy.random.uniform(size=3)
    a/= numpy.sqrt(numpy.sum(a**2.))
    ma= streamgapdf._rotate_to_arbitrary_vector(v,a)
    ma_inv= streamgapdf._rotate_to_arbitrary_vector(v,a,inv=True)
    ma= numpy.dot(ma[0],ma_inv[0])
    assert numpy.all(numpy.fabs(ma-numpy.eye(3)) < 10.**tol), 'Inverse rotation matrix incorrect'
    return None

# Test that rotating to vy in particular works as expected
def test_rotation_vy():
    from galpy.df_src import streamgapdf
    tol= -10.
    v= numpy.array([[1.,0.,0.]])
    # Rotate to 90 deg off
    ma= streamgapdf._rotation_vy(v)
    assert numpy.fabs(ma[0,0,1]+1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,0]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,2]-1.) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,0,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,1,2]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,0]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'
    assert numpy.fabs(ma[0,2,1]) < 10.**tol, 'Rotation matrix to 90 deg off incorrect'

# Test the Plummer calculation for a perpendicular impact, B&T ex. 8.7
def test_impulse_deltav_plummer_subhalo_perpendicular():
    from galpy.df_src import streamgapdf
    tol= -10.
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[0.,numpy.pi,0.]]),
                                             numpy.array([0.]),
                                             3.,
                                             numpy.array([0.,numpy.pi/2.,0.]),
                                             1.5,4.)
    # Should be B&T (8.152)
    assert numpy.fabs(kick[0,0]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    assert numpy.fabs(kick[0,2]+2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    # Same for along z
    kick= streamgapdf.impulse_deltav_plummer(numpy.array([[0.,0.,numpy.pi]]),
                                             numpy.array([0.]),
                                             3.,
                                             numpy.array([0.,0.,numpy.pi/2.]),
                                             1.5,4.)
    # Should be B&T (8.152)
    assert numpy.fabs(kick[0,0]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    assert numpy.fabs(kick[0,1]-2.*1.5*3./numpy.pi*2./25.) < 10.**tol, 'Perpendicular kick of subhalo perpendicular not as expected'
    return None