# Concept

This file is filled with bullshit. Ignore it.

## Networking
The base terminal runs few goprocs, first is a server which helps process things with the os. This should technically be the parent-ish process as it will be doing all the cool things with the disk. The server communicates with clients over gob or something similar and is pretty simple. The server pushes rendering and such to the frontend. That means we need the following for the server

- Buffering of images/video/audio clips
- Multiple channel communication (COMMAND, DATA, BUFFER)
- Multiple clients? Screen like behaivor then?

## Graphics
Build out a /very/ basic gui with some utilitys for framing content and resizing. Include API's for drawing raw 2d/3d content to the display.

TODO: Decided what rendering to do. OpenGL? SDL? Allegro? WAT?

Don't suck at text scaling/DPI scaling

## Lua Scripting
Multiple types of scripting, maybe have to write extensions on top?

- https://github.com/stevedonovan/Penlight
- https://github.com/kikito/middleclass

### CLI Scripting
Basically what bash should be...

rm -rf *
```lua
dir = fk.ls()

dir.map(function (i) fk.rm(i, force=true) end)
```

### Config Scripting

Rule to prefer configure over config in autocomplete
```lua
fk.autocom.add_handler("config", function (frame, choices) 
    if choices.contains("configure") and choices.contains("config") then
        choices.rank("configure", choices.get("config").rank - 1)
    end
end)
```

Simple aliases
```lua
fk.alias("e", "emacs", args={"n", "w"})
```

Magic shit w/ git
```lua
function check_gh_updates(git)
    -- blahhhhhhh
    res = fk.ui.prompt("Changes detected to git repo on the current branch. Pull?", yn=true)
    if res then
        git.pull()
    end
end

fk.dir.on("change". function (old_dir, new_dir)
    if new_dir.ls().contains(".git") then
        git = fk.git.open(new_dir)
        git.remotes.map(function (i)
            if i.url.contains("github.com") then
                return check_gh_updates(git)
            end
        end)
    end
end)
