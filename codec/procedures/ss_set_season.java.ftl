if(world instanceof ServerLevel _level) _level.getServer().getCommands().performPrefixedCommand(new CommandSourceStack(CommandSource.NULL, new Vec3(${input$X}, ${input$Y}, ${input$Z}), Vec2.ZERO, _level, 4, "", Component.literal(""), _level.getServer(), null).withSuppressedOutput(), "set season ${field$season}");