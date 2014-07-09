package main

import "./fkt"
import "time"

func main() {
	term := fkt.NewTerminal()
	term.RunCLI()
	for {
		time.Sleep(time.Second * 5)
	}
}
