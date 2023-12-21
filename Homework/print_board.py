def print_board(tower_1, tower_2, tower_3, moves):
    print("Tower 1:            Tower 2:            Tower 3:            ")
    if len(tower_1) < 8:
        print("          |          ", end = "")
    elif tower_1[7] == 8:
        print("          *          ", end = "")
    if len(tower_2) < 8:
        print("          |          ", end = "")
    elif tower_2[7] == 8:
        print("          *          ", end = "")
    if len(tower_3) < 8:
        print("          |          ")
    elif tower_3[7] == 8:
        print("          *          ")
    if len(tower_1) < 7:
        print("          |          ", end = "")
    elif tower_1[6] == 8:
        print("          *          ", end = "")
    elif tower_1[6] == 7:
        print("         * *         ", end = "")
    if len(tower_2) < 7:
        print("          |          ", end = "")
    elif tower_2[6] == 8:
        print("          *          ", end = "")
    elif tower_2[6] == 7:
        print("         * *         ", end = "")
    if len(tower_3) < 7:
        print("          |          ")
    elif tower_3[6] == 8:
        print("          *          ")
    elif tower_3[6] == 7:
        print("         * *         ")
    if len(tower_1) < 6:
        print("          |          ", end = "")
    elif tower_1[5] == 8:
        print("          *          ", end = "")
    elif tower_1[5] == 7:
        print("         * *         ", end = "")
    elif tower_1[5] == 6:
        print("        * * *        ", end = "")
    if len(tower_2) < 6:
        print("          |          ", end = "")
    elif tower_2[5] == 8:
        print("          *          ", end = "")
    elif tower_2[5] == 7:
        print("         * *         ", end = "")
    elif tower_2[5] == 6:
        print("        * * *        ", end = "")
    if len(tower_3) < 6:
        print("          |          ")
    elif tower_3[5] == 8:
        print("          *          ")
    elif tower_3[5] == 7:
        print("         * *         ")
    elif tower_3[5] == 6:
        print("        * * *        ")
    if len(tower_1) < 5:
        print("          |          ", end = "")
    elif tower_1[4] == 8:
        print("          *          ", end = "")
    elif tower_1[4] == 7:
        print("         * *         ", end = "")
    elif tower_1[4] == 6:
        print("        * * *        ", end = "")
    elif tower_1[4] == 5:
        print("       * * * *       ", end = "")
    if len(tower_2) < 5:
        print("          |          ", end = "")
    elif tower_2[4] == 8:
        print("          *          ", end = "")
    elif tower_2[4] == 7:
        print("         * *         ", end = "")
    elif tower_2[4] == 6:
        print("        * * *        ", end = "")
    elif tower_2[4] == 5:
        print("       * * * *       ", end = "")
    if len(tower_3) < 5:
        print("          |          ")
    elif tower_3[4] == 8:
        print("          *          ")
    elif tower_3[4] == 7:
        print("         * *         ")
    elif tower_3[4] == 6:
        print("        * * *        ")
    elif tower_3[4] == 5:
        print("       * * * *       ")
    if len(tower_1) < 4:
        print("          |          ", end = "")
    elif tower_1[3] == 8:
        print("          *          ", end = "")
    elif tower_1[3] == 7:
        print("         * *         ", end = "")
    elif tower_1[3] == 6:
        print("        * * *        ", end = "")
    elif tower_1[3] == 5:
        print("       * * * *       ", end = "")
    elif tower_1[3] == 4:
        print("      * * * * *      ", end = "")
    if len(tower_2) < 4:
        print("          |          ", end = "")
    elif tower_2[3] == 8:
        print("          *          ", end = "")
    elif tower_2[3] == 7:
        print("         * *         ", end = "")
    elif tower_2[3] == 6:
        print("        * * *        ", end = "")
    elif tower_2[3] == 5:
        print("       * * * *       ", end = "")
    elif tower_2[3] == 4:
        print("      * * * * *      ", end = "")
    if len(tower_3) < 4:
        print("          |          ")
    elif tower_3[3] == 8:
        print("          *          ")
    elif tower_3[3] == 7:
        print("         * *         ")
    elif tower_3[3] == 6:
        print("        * * *        ")
    elif tower_3[3] == 5:
        print("       * * * *       ")
    elif tower_3[3] == 4:
        print("      * * * * *      ")
    if len(tower_1) < 3:
        print("          |          ", end = "")
    elif tower_1[2] == 8:
        print("          *          ", end = "")
    elif tower_1[2] == 7:
        print("         * *         ", end = "")
    elif tower_1[2] == 6:
        print("        * * *        ", end = "")
    elif tower_1[2] == 5:
        print("       * * * *       ", end = "")
    elif tower_1[2] == 4:
        print("      * * * * *      ", end = "")
    elif tower_1[2] == 3:
        print("     * * * * * *     ", end = "")
    if len(tower_2) < 3:
        print("          |          ", end = "")
    elif tower_2[2] == 8:
        print("          *          ", end = "")
    elif tower_2[2] == 7:
        print("         * *         ", end = "")
    elif tower_2[2] == 6:
        print("        * * *        ", end = "")
    elif tower_2[2] == 5:
        print("       * * * *       ", end = "")
    elif tower_2[2] == 4:
        print("      * * * * *      ", end = "")
    elif tower_2[2] == 3:
        print("     * * * * * *     ", end = "")
    if len(tower_3) < 3:
        print("          |          ")
    elif tower_3[2] == 8:
        print("          *          ")
    elif tower_3[2] == 7:
        print("         * *         ")
    elif tower_3[2] == 6:
        print("        * * *        ")
    elif tower_3[2] == 5:
        print("       * * * *       ")
    elif tower_3[2] == 4:
        print("      * * * * *      ")
    elif tower_3[2] == 3:
        print("     * * * * * *     ")
    if len(tower_1) < 2:
        print("          |          ", end = "")
    elif tower_1[1] == 8:
        print("          *          ", end = "")
    elif tower_1[1] == 7:
        print("         * *         ", end = "")
    elif tower_1[1] == 6:
        print("        * * *        ", end = "")
    elif tower_1[1] == 5:
        print("       * * * *       ", end = "")
    elif tower_1[1] == 4:
        print("      * * * * *      ", end = "")
    elif tower_1[1] == 3:
        print("     * * * * * *     ", end = "")
    elif tower_1[1] == 2:
        print("    * * * * * * *    ", end = "")
    if len(tower_2) < 2:
        print("          |          ", end = "")
    elif tower_2[1] == 8:
        print("          *          ", end = "")
    elif tower_2[1] == 7:
        print("         * *         ", end = "")
    elif tower_2[1] == 6:
        print("        * * *        ", end = "")
    elif tower_2[1] == 5:
        print("       * * * *       ", end = "")
    elif tower_2[1] == 4:
        print("      * * * * *      ", end = "")
    elif tower_2[1] == 3:
        print("     * * * * * *     ", end = "")
    elif tower_2[1] == 2:
        print("    * * * * * * *    ", end = "")
    if len(tower_3) < 2:
        print("          |          ")
    elif tower_3[1] == 8:
        print("          *          ")
    elif tower_3[1] == 7:
        print("         * *         ")
    elif tower_3[1] == 6:
        print("        * * *        ")
    elif tower_3[1] == 5:
        print("       * * * *       ")
    elif tower_3[1] == 4:
        print("      * * * * *      ")
    elif tower_3[1] == 3:
        print("     * * * * * *     ")
    elif tower_3[1] == 2:
        print("    * * * * * * *    ")
    if len(tower_1) < 1:
        print("          |          ", end = "")
    elif tower_1[0] == 8:
        print("          *          ", end = "")
    elif tower_1[0] == 7:
        print("         * *         ", end = "")
    elif tower_1[0] == 6:
        print("        * * *        ", end = "")
    elif tower_1[0] == 5:
        print("       * * * *       ", end = "")
    elif tower_1[0] == 4:
        print("      * * * * *      ", end = "")
    elif tower_1[0] == 3:
        print("     * * * * * *     ", end = "")
    elif tower_1[0] == 2:
        print("    * * * * * * *    ", end = "")
    elif tower_1[0] == 1:
        print("   * * * * * * * *   ", end = "")
    if len(tower_2) < 1:
        print("          |          ", end = "")
    elif tower_2[0] == 8:
        print("          *          ", end = "")
    elif tower_2[0] == 7:
        print("         * *         ", end = "")
    elif tower_2[0] == 6:
        print("        * * *        ", end = "")
    elif tower_2[0] == 5:
        print("       * * * *       ", end = "")
    elif tower_2[0] == 4:
        print("      * * * * *      ", end = "")
    elif tower_2[0] == 3:
        print("     * * * * * *     ", end = "")
    elif tower_2[0] == 2:
        print("    * * * * * * *    ", end = "")
    elif tower_2[0] == 1:
        print("   * * * * * * * *   ", end = "")
    if len(tower_3) < 1:
        print("          |          ")
    elif tower_3[0] == 8:
        print("          *          ")
    elif tower_3[0] == 7:
        print("         * *         ")
    elif tower_3[0] == 6:
        print("        * * *        ")
    elif tower_3[0] == 5:
        print("       * * * *       ")
    elif tower_3[0] == 4:
        print("      * * * * *      ")
    elif tower_3[0] == 3:
        print("     * * * * * *     ")
    elif tower_3[0] == 2:
        print("    * * * * * * *    ")
    elif tower_3[0] == 1:
        print("   * * * * * * * *   ")
    print("  -----------------    -----------------    -----------------  ")
    print("Moves: ", moves)