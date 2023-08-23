def solution(wallpaper):
    miny=maxy=maxx=-1
    minx=len(wallpaper[0])
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            if miny == -1: miny = i
            maxy = max(maxy, i)
            minx = min(minx, wallpaper[i].index("#"))
            maxx = max(maxx, wallpaper[i].rindex("#"))
    return [miny, minx, maxy+1, maxx+1]