def color_elevation_check(par):
    if par < 1000:
        return 'green'
    elif 1000 <= par <3000:
        return 'orange'
    else:
        return 'red'