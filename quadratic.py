def quadratic(a=None, b=None, c=None, large=False):
    """ minimilist quadratic solution as root for J solution should always
    be positive, so I have excluded other quadratic solution steps. I am
    only returning the smallest of the two roots

    Parameters:
    ----------
    a : float
        co-efficient
    b : float
        co-efficient
    c : float
        co-efficient

    Returns:
    -------
    val : float
        positive root
    """
    d = b**2.0 - 4.0 * a * c # discriminant
    if d < 0.0:
        raise ValueError('imaginary root found')
    #root1 = np.where(d>0.0, (-b - np.sqrt(d)) / (2.0 * a), d)
    #root2 = np.where(d>0.0, (-b + np.sqrt(d)) / (2.0 * a), d)

    if large:
        if math.isclose(a, 0.0) and b > 0.0:
            root = -c / b
        elif math.isclose(a, 0.0) and math.isclose(b, 0.0):
            root = 0.0
            if c != 0.0:
                raise ValueError('Cant solve quadratic')
        else:
            root = (-b + np.sqrt(d)) / (2.0 * a)
    else:
        if math.isclose(a, 0.0) and b > 0.0:
            root = -c / b
        elif math.isclose(a, 0.0) and math.isclose(b, 0.0):
            root == 0.0
            if c != 0.0:
                raise ValueError('Cant solve quadratic')
        else:
            root = (-b - np.sqrt(d)) / (2.0 * a)

    return root
