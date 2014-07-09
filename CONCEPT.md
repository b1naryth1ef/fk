# Concept

This file is filled with bullshit. Ignore it.

## Tidbits

FKT RUNNING IN FKT? IS IT EVEN POSSIBLE?

## Autocomplete
Who even knows how this should work. I think the best way is to allow fk-based programs too define fk-ac files, bash completion? watdafuq?

## Keybindings
By default, only bind ctrl+enter as the command runner, let people build out their own fucking default configs (or provide bash-ish configs w/ ctrl+c etc).

## Processes
Don't just use the old open-quit standard, allow sleeping and idle processes of some sort. Fuck if I know how this should work lewl.

## Pipes/etc
SHOULD BE SMARTER AND SUCK LESS. We (in theory) could make this shit channels and then pipe over zmq. Would be crazy but might work, not sure about local performance (server perf would suck penis but at least it would work)

## Networking
The base terminal runs few goprocs, first is a server which helps process things with the os. This should technically be the parent-ish process as it will be doing all the cool things with the disk. The server communicates with clients over gob or something similar and is pretty simple. The server pushes rendering and such to the frontend. That means we need the following for the server

- Buffering of images/video/audio clips
- Multiple channel communication (COMMAND, DATA, BUFFER)
- Multiple clients? Screen like behaivor then?

## Graphics
Build out a /very/ basic gui with some utilitys for framing content and resizing. Include API's for drawing raw 2d/3d content to the display.

TODO: Decided what rendering to do. OpenGL? SDL? Allegro? WAT?

Don't suck at text scaling/DPI scaling

### Drawing Modes

#### GUI

Windows? Borders? Headers?

Allow some sort of interface definition that would let it handle some basic GUI stuff like prompts/titles/warnings/alerts. Would be awesome to make /some/ kind of standard for this

#### Text Based

- set_char(x, y, char, {font, style})
- set_fg_color(x, y, color)
- set_bg_color(x, y, color)
- clear()

- create_region(name, h, w)
- delete_region(name)
- region.set_text({})
- region.render(x, y)
- etc...

#### 2d

- draw_box(x, y, h, w, params)
- draw_circle(...)
- draw_line(...)
- draw_poly(...)
- draw_image(img_content)


#### 3d
Will this be possible? Seems like a shitload of network weight. We need to investigate this before doing it. Would be /insanely/ awesome to support movie streams or the sort. Unlikely, but lets look into it for local-fk. (e.g. open my_porno.mkv and it plays in screen)


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


## Example Implementations

- basic bash (ls, rm, mkdir, mv, etc...)
- complex bash (top?)
- fk-app (editor? etc?)
- fk-2d (game? gnuplot? vlc (WAT?)?)
- fk-3d (...)


## Stages

1. Basic bash support and drawing, I want to touch a file, cat a file, rm a file and mv a file.
2. 2d rendering support, the fk-app protocol should be defined and workingish
3. ??????????
4. FKT RUNNING INSIDE FKT WWAAAAATTT!!!!!?!?!?!?!