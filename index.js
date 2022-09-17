#!/usr/bin/env node

import chalk from 'chalk';
import inquirer from 'inquirer';
import gradient from 'gradient-string';
import figlet from 'figlet';
import { table } from 'table';

const cords = {
    top: 0,
    left: 0,
    mid: 1,
    right: 2,
    bot: 2,
}

const PLAYERS = {
    X: "X",
    O: "O"
}

let player = PLAYERS.O
let game = [
    [[["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]]],
    [[["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]]],
    [[["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]],
    [["", "", ""], ["", "", ""], ["", "", ""]]],
]

const sleep = (ms = 2000) => new Promise((r) => setTimeout(r, ms))

const printGame = () => {
    const data = game.map((item) => item.map((it) => table(it)))

    console.log(table(data))
}

const printBoard = (boardCords) => {
    console.log(table(game[boardCords.x][boardCords.y]))
}

const boardWonByPlayer = (boardCords, selectedPlayer) => {
    const board = game[boardCords.x][boardCords.y]

    return board[cords.top][cords.left] === selectedPlayer && board[cords.top][cords.mid] === selectedPlayer && board[cords.top][cords.right] === selectedPlayer ||
        board[cords.mid][cords.left] === selectedPlayer && board[cords.mid][cords.mid] === selectedPlayer && board[cords.mid][cords.right] === selectedPlayer ||
        board[cords.bot][cords.left] === selectedPlayer && board[cords.bot][cords.mid] === selectedPlayer && board[cords.bot][cords.right] === selectedPlayer ||
        board[cords.top][cords.left] === selectedPlayer && board[cords.mid][cords.left] === selectedPlayer && board[cords.bot][cords.left] === selectedPlayer ||
        board[cords.top][cords.mid] === selectedPlayer && board[cords.mid][cords.mid] === selectedPlayer && board[cords.bot][cords.mid] === selectedPlayer ||
        board[cords.top][cords.right] === selectedPlayer && board[cords.mid][cords.right] === selectedPlayer && board[cords.bot][cords.right] === selectedPlayer ||
        board[cords.top][cords.left] === selectedPlayer && board[cords.mid][cords.mid] === selectedPlayer && board[cords.bot][cords.right] === selectedPlayer ||
        board[cords.bot][cords.left] === selectedPlayer && board[cords.mid][cords.mid] === selectedPlayer && board[cords.top][cords.right] === selectedPlayer
}

const boardWon = (boardCords) => {
    return boardWonByPlayer(boardCords, PLAYERS.O) || boardWonByPlayer(boardCords, PLAYERS.X)
}

const gameWon = () => {
    return boardWon({ x: cords.top, y: cords.left }) && boardWon({ x: cords.top, y: cords.mid }) && boardWon({ x: cords.top, y: cords.right }) ||
        boardWon({ x: cords.mid, y: cords.left }) && boardWon({ x: cords.mid, y: cords.mid }) && boardWon({ x: cords.mid, y: cords.right }) ||
        boardWon({ x: cords.bot, y: cords.left }) && boardWon({ x: cords.bot, y: cords.mid }) && boardWon({ x: cords.bot, y: cords.right }) ||
        boardWon({ x: cords.top, y: cords.left }) && boardWon({ x: cords.mid, y: cords.left }) && boardWon({ x: cords.bot, y: cords.left }) ||
        boardWon({ x: cords.top, y: cords.left }) && boardWon({ x: cords.mid, y: cords.mid }) && boardWon({ x: cords.bot, y: cords.mid }) ||
        boardWon({ x: cords.top, y: cords.left }) && boardWon({ x: cords.mid, y: cords.right }) && boardWon({ x: cords.bot, y: cords.right }) ||
        boardWon({ x: cords.top, y: cords.left }) && boardWon({ x: cords.mid, y: cords.mid }) && boardWon({ x: cords.bot, y: cords.right }) ||
        boardWon({ x: cords.bot, y: cords.left }) && boardWon({ x: cords.mid, y: cords.mid }) && boardWon({ x: cords.top, y: cords.right })

}

const boardDrawn = (boardCords) => {
    if (boardCords.x === -1) {
        return false
    }

    return !game[boardCords.x][boardCords.y].some((col) => col.some((row) => row === ""))
}

const isValidBoard = (boardCords) => {
    if (boardCords.x === -1) {
        return false
    }


    if (boardWon(boardCords) || boardDrawn(boardCords)) {
        return false
    }

    return true
}

const convertInputToCords = (input) => {
    switch (input) {
        case 1: return { x: 2, y: 0 }
        case 2: return { x: 2, y: 1 }
        case 3: return { x: 2, y: 2 }
        case 4: return { x: 1, y: 0 }
        case 5: return { x: 1, y: 1 }
        case 6: return { x: 1, y: 2 }
        case 7: return { x: 0, y: 0 }
        case 8: return { x: 0, y: 1 }
        case 9: return { x: 0, y: 2 }
        default: return { x: -1, y: -1 }
    }
}

const gameDrawn = () => {
    for (let i = 1; i < 10; i++) {
        if (isValidBoard(convertInputToCords(i))) {
            return false
        }
    }

    return true
}

const gameOver = () => {
    return gameWon() || gameDrawn()
}

const welcome = async () => {
    console.clear()
    const welcome = "Tic - Tac - Toe 2"

    figlet(welcome, (_, data) => {
        console.log(gradient.pastel.multiline(data))
    })

    await sleep()
}

const goodbye = () => {
    const goodbye = `Player ${player} won the game!`

    figlet(goodbye, (_, data) => {
        console.log(gradient.morning.multiline(data))
    })
}

const selectBoard = async (boardCords) => {
    while (!isValidBoard(boardCords)) {
        const answer = await inquirer.prompt({
            name: "selectedBoard",
            type: "number",
            message: "Please select a board."
        })

        boardCords = convertInputToCords(answer.selectedBoard)
    }

    return boardCords
}

const isValidField = (boardCoords, fieldCords) => {
    if (fieldCords.x === -1) {
        return false
    }

    return game[boardCoords.x][boardCoords.y][fieldCords.x][fieldCords.y] === ""
}

const selectField = async (boardCords, fieldCords) => {
    while (!isValidField(boardCords, fieldCords)) {
        const answer = await inquirer.prompt({
            name: "selectedField",
            type: "number",
            message: "Please select a field."
        })

        fieldCords = convertInputToCords(answer.selectedField)
    }

    return fieldCords
}

const convertCordsToInput = (cords) => {
    if (cords.x === 2 && cords.y === 0) {
        return 1
    } else if (cords.x === 2 && cords.y === 1) {
        return 2
    } else if (cords.x === 2 && cords.y === 2) {
        return 3
    } else if (cords.x === 1 && cords.y === 0) {
        return 4
    } else if (cords.x === 1 && cords.y === 1) {
        return 5
    } else if (cords.x === 1 && cords.y === 2) {
        return 6
    } else if (cords.x === 0 && cords.y === 0) {
        return 7
    } else if (cords.x === 0 && cords.y === 1) {
        return 8
    } else if (cords.x === 0 && cords.y === 2) {
        return 9
    } else {
        return -1
    }
}

const run_game = async () => {
    await welcome()

    let boardCords = { x: -1, y: -1 }

    while (!gameOver()) {
        player = player === PLAYERS.X ? PLAYERS.O : PLAYERS.X

        printGame()

        console.log(chalk.bgBlue(`It is player ${player}\'s turn!`))

        await sleep(100)

        if (!isValidBoard(boardCords)) {
            boardCords = await selectBoard(boardCords)
        }

        printBoard(boardCords)

        let fieldCords = { x: -1, y: -1 }
        fieldCords = await selectField(boardCords, fieldCords)
        game[boardCords.x][boardCords.y][fieldCords.x][fieldCords.y] = player

        if (boardWonByPlayer(boardCords, player)) {
            console.log(chalk.bgGreen(`Player ${player} won board ${convertCordsToInput(boardCords)}!`))
        } else if (boardDrawn(boardCords)) {
            console.log(chalk.bgGray(`Board ${convertCordsToInput(boardCords)} ended in a draw!`))
        }

        boardCords = fieldCords
    }

    if (gameWon) {
        goodbye()
    } else {
        console.log(gradient.passion("The game ended in a draw!"))
    }
}

await run_game()
