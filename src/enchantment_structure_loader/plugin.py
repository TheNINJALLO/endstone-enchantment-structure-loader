from endstone.plugin import Plugin

ENCHANTMENT_ITEMS = [
    {"id": "z:banearthropodsviii", "structure": "banearthropods/viii"},
    {"id": "z:banearthropodsvi", "structure": "banearthropods/vi"},
    {"id": "z:banearthropodsix", "structure": "banearthropods/ix"},
    {"id": "z:banearthropodsx", "structure": "banearthropods/x"},
    {"id": "z:banearthropodsvii", "structure": "banearthropods/vii"},
    {"id": "z:depthstrideriv", "structure": "depthstrider/iv"},
    {"id": "z:depthstridervi", "structure": "depthstrider/vi"},
    {"id": "z:depthstriderv", "structure": "depthstrider/v"},
    {"id": "z:depthstriderviii", "structure": "depthstrider/viii"},
    {"id": "z:depthstriderix", "structure": "depthstrider/ix"},
    {"id": "z:depthstriderx", "structure": "depthstrider/x"},
    {"id": "z:depthstridervii", "structure": "depthstrider/vii"},
    {"id": "z:efficiencyvii", "structure": "efficiency/vii"},
    {"id": "z:efficiencyix", "structure": "efficiency/ix"},
    {"id": "z:efficiencyvi", "structure": "efficiency/vi"},
    {"id": "z:efficiencyviii", "structure": "efficiency/viii"},
    {"id": "z:efficiencyx", "structure": "efficiency/x"},
    {"id": "z:featherfallingvi", "structure": "featherfalling/vi"},
    {"id": "z:featherfallingviii", "structure": "featherfalling/viii"},
    {"id": "z:featherfallingv", "structure": "featherfalling/v"},
    {"id": "z:featherfallingx", "structure": "featherfalling/x"},
    {"id": "z:featherfallingvii", "structure": "featherfalling/vii"},
    {"id": "z:featherfallingix", "structure": "featherfalling/ix"},
    {"id": "z:fireaspectiv", "structure": "fireaspect/iv"},
    {"id": "z:fireaspectix", "structure": "fireaspect/ix"},
    {"id": "z:fireaspectiii", "structure": "fireaspect/iii"},
    {"id": "z:fireaspectv", "structure": "fireaspect/v"},
    {"id": "z:fireaspectvi", "structure": "fireaspect/vi"},
    {"id": "z:fireaspectviii", "structure": "fireaspect/viii"},
    {"id": "z:fireaspectvii", "structure": "fireaspect/vii"},
    {"id": "z:fireaspectx", "structure": "fireaspect/x"},
    {"id": "z:fortunev", "structure": "fortune/v"},
    {"id": "z:fortuneiv", "structure": "fortune/iv"},
    {"id": "z:fortunex", "structure": "fortune/x"},
    {"id": "z:fortunevi", "structure": "fortune/vi"},
    {"id": "z:fortunevii", "structure": "fortune/vii"},
    {"id": "z:fortuneviii", "structure": "fortune/viii"},
    {"id": "z:fortuneix", "structure": "fortune/ix"},
    {"id": "z:frostwalkerix", "structure": "frostwalker/ix"},
    {"id": "z:frostwalkeriv", "structure": "frostwalker/iv"},
    {"id": "z:frostwalkervi", "structure": "frostwalker/vi"},
    {"id": "z:frostwalkerv", "structure": "frostwalker/v"},
    {"id": "z:frostwalkeriii", "structure": "frostwalker/iii"},
    {"id": "z:frostwalkerviii", "structure": "frostwalker/viii"},
    {"id": "z:frostwalkervii", "structure": "frostwalker/vii"},
    {"id": "z:frostwalkerx", "structure": "frostwalker/x"},
    {"id": "z:impalingix", "structure": "impaling/ix"},
    {"id": "z:impalingx", "structure": "impaling/x"},
    {"id": "z:impalingvii", "structure": "impaling/vii"},
    {"id": "z:impalingvi", "structure": "impaling/vi"},
    {"id": "z:impalingviii", "structure": "impaling/viii"},
    {"id": "z:knockbackviii", "structure": "knockback/viii"},
    {"id": "z:knockbackv", "structure": "knockback/v"},
    {"id": "z:knockbackvii", "structure": "knockback/vii"},
    {"id": "z:knockbackiii", "structure": "knockback/iii"},
    {"id": "z:knockbackix", "structure": "knockback/ix"},
    {"id": "z:knockbackiv", "structure": "knockback/iv"},
    {"id": "z:knockbackx", "structure": "knockback/x"},
    {"id": "z:knockbackvi", "structure": "knockback/vi"},
    {"id": "z:lootingiv", "structure": "looting/iv"},
    {"id": "z:lootingvi", "structure": "looting/vi"},
    {"id": "z:lootingv", "structure": "looting/v"},
    {"id": "z:lootingix", "structure": "looting/ix"},
    {"id": "z:lootingviii", "structure": "looting/viii"},
    {"id": "z:lootingvii", "structure": "looting/vii"},
    {"id": "z:lootingx", "structure": "looting/x"},
    {"id": "z:loyalityx", "structure": "loyality/x"},
    {"id": "z:loyalityvi", "structure": "loyality/vi"},
    {"id": "z:loyalityix", "structure": "loyality/ix"},
    {"id": "z:loyalityvii", "structure": "loyality/vii"},
    {"id": "z:loyalityv", "structure": "loyality/v"},
    {"id": "z:loyalityiv", "structure": "loyality/iv"},
    {"id": "z:loyalityviii", "structure": "loyality/viii"},
    {"id": "z:luckseax", "structure": "lucksea/x"},
    {"id": "z:luckseavii", "structure": "lucksea/vii"},
    {"id": "z:luckseav", "structure": "lucksea/v"},
    {"id": "z:luckseaviii", "structure": "lucksea/viii"},
    {"id": "z:luckseaix", "structure": "lucksea/ix"},
    {"id": "z:luckseavi", "structure": "lucksea/vi"},
    {"id": "z:luckseaiv", "structure": "lucksea/iv"},
    {"id": "z:lureiv", "structure": "lure/iv"},
    {"id": "z:lurev", "structure": "lure/v"},
    {"id": "z:piercingviii", "structure": "piercing/viii"},
    {"id": "z:piercingvi", "structure": "piercing/vi"},
    {"id": "z:piercingix", "structure": "piercing/ix"},
    {"id": "z:piercingvii", "structure": "piercing/vii"},
    {"id": "z:piercingv", "structure": "piercing/v"},
    {"id": "z:piercingx", "structure": "piercing/x"},
    {"id": "z:powervii", "structure": "power/vii"},
    {"id": "z:powerviii", "structure": "power/viii"},
    {"id": "z:powervi", "structure": "power/vi"},
    {"id": "z:powerix", "structure": "power/ix"},
    {"id": "z:powerx", "structure": "power/x"},
    {"id": "z:protectionx", "structure": "protection/x"},
    {"id": "z:protectionvi", "structure": "protection/vi"},
    {"id": "z:protectionvii", "structure": "protection/vii"},
    {"id": "z:protectionix", "structure": "protection/ix"},
    {"id": "z:protectionxi", "structure": "protection/x"},
    {"id": "z:protectionviii", "structure": "protection/viii"},
    {"id": "z:protectionxii", "structure": "protection/x"},
    {"id": "z:protectionv", "structure": "protection/v"},
    {"id": "z:protectionxiii", "structure": "protection/x"},
    {"id": "z:protectionxiv", "structure": "protection/x"},
    {"id": "z:protectionxix", "structure": "protection/x"},
    {"id": "z:protectionxv", "structure": "protection/x"},
    {"id": "z:protectionxvii", "structure": "protection/x"},
    {"id": "z:protectionxx", "structure": "protection/x"},
    {"id": "z:protectionxvi", "structure": "protection/x"},
    {"id": "z:protectionxviii", "structure": "protection/x"},
    {"id": "z:protectionexplv", "structure": "protectionexpl/v"},
    {"id": "z:protectionexplvii", "structure": "protectionexpl/vii"},
    {"id": "z:protectionexplx", "structure": "protectionexpl/x"},
    {"id": "z:protectionexplviii", "structure": "protectionexpl/viii"},
    {"id": "z:protectionexplix", "structure": "protectionexpl/ix"},
    {"id": "z:protectionexplvi", "structure": "protectionexpl/vi"},
    {"id": "z:protectionfireix", "structure": "protectionfire/ix"},
    {"id": "z:protectionfirevi", "structure": "protectionfire/vi"},
    {"id": "z:protectionfirev", "structure": "protectionfire/v"},
    {"id": "z:protectionfireviii", "structure": "protectionfire/viii"},
    {"id": "z:protectionfirevii", "structure": "protectionfire/vii"},
    {"id": "z:protectionfirex", "structure": "protectionfire/x"},
    {"id": "z:protectionprojviii", "structure": "protectionproj/viii"},
    {"id": "z:protectionprojix", "structure": "protectionproj/ix"},
    {"id": "z:protectionprojx", "structure": "protectionproj/x"},
    {"id": "z:protectionprojvi", "structure": "protectionproj/vi"},
    {"id": "z:protectionprojv", "structure": "protectionproj/v"},
    {"id": "z:protectionprojvii", "structure": "protectionproj/vii"},
    {"id": "z:punchvii", "structure": "punch/vii"},
    {"id": "z:punchiii", "structure": "punch/iii"},
    {"id": "z:punchvi", "structure": "punch/vi"},
    {"id": "z:punchiv", "structure": "punch/iv"},
    {"id": "z:punchv", "structure": "punch/v"},
    {"id": "z:punchviii", "structure": "punch/viii"},
    {"id": "z:punchx", "structure": "punch/x"},
    {"id": "z:punchix", "structure": "punch/ix"},
    {"id": "z:quickchargeiv", "structure": "quickcharge/iv"},
    {"id": "z:quickchargev", "structure": "quickcharge/iv"},
    {"id": "z:respirationvii", "structure": "respiration/vii"},
    {"id": "z:respirationiv", "structure": "respiration/iv"},
    {"id": "z:respirationx", "structure": "respiration/x"},
    {"id": "z:respirationix", "structure": "respiration/ix"},
    {"id": "z:respirationv", "structure": "respiration/v"},
    {"id": "z:respirationvi", "structure": "respiration/vi"},
    {"id": "z:respirationviii", "structure": "respiration/viii"},
    {"id": "z:riptideiv", "structure": "riptide/iv"},
    {"id": "z:riptidevii", "structure": "riptide/vii"},
    {"id": "z:riptidev", "structure": "riptide/v"},
    {"id": "z:firetidei", "structure": "riptide/firetidei"},
    {"id": "z:riptideix", "structure": "riptide/ix"},
    {"id": "z:riptidevi", "structure": "riptide/vi"},
    {"id": "z:riptidex", "structure": "riptide/x"},
    {"id": "z:riptideviii", "structure": "riptide/viii"},
    {"id": "z:sharpnessix", "structure": "sharpness/ix"},
    {"id": "z:sharpnessvi", "structure": "sharpness/vi"},
    {"id": "z:sharpnessx", "structure": "sharpness/x"},
    {"id": "z:sharpnessviii", "structure": "sharpness/viii"},
    {"id": "z:sharpnessvii", "structure": "sharpness/vii"},
    {"id": "z:smitex", "structure": "smite/x"},
    {"id": "z:smitevi", "structure": "smite/vi"},
    {"id": "z:smiteviii", "structure": "smite/viii"},
    {"id": "z:smiteix", "structure": "smite/ix"},
    {"id": "z:smitevii", "structure": "smite/vii"},
    {"id": "z:soulspeedvii", "structure": "soulspeed/vii"},
    {"id": "z:soulspeediv", "structure": "soulspeed/iv"},
    {"id": "z:soulspeedix", "structure": "soulspeed/ix"},
    {"id": "z:soulspeedv", "structure": "soulspeed/v"},
    {"id": "z:soulspeedx", "structure": "soulspeed/x"},
    {"id": "z:soulspeedviii", "structure": "soulspeed/viii"},
    {"id": "z:soulspeedvi", "structure": "soulspeed/vi"},
    {"id": "z:swiftsneakiv", "structure": "swiftsneak/iv"},
    {"id": "z:swiftsneakv", "structure": "swiftsneak/v"},
    {"id": "z:thornsx", "structure": "thorns/x"},
    {"id": "z:thornsix", "structure": "thorns/ix"},
    {"id": "z:thornsiv", "structure": "thorns/iv"},
    {"id": "z:thornsviii", "structure": "thorns/viii"},
    {"id": "z:thornsvi", "structure": "thorns/vi"},
    {"id": "z:thornsvii", "structure": "thorns/vii"},
    {"id": "z:thornsv", "structure": "thorns/v"},
    {"id": "z:unbreakingiv", "structure": "unbreaking/iv"},
    {"id": "z:unbreakingix", "structure": "unbreaking/ix"},
    {"id": "z:unbreakingvi", "structure": "unbreaking/vi"},
    {"id": "z:unbreakingv", "structure": "unbreaking/v"},
    {"id": "z:unbreakingvii", "structure": "unbreaking/vii"},
    {"id": "z:unbreakingviii", "structure": "unbreaking/viii"},
    {"id": "z:unbreakingx", "structure": "unbreaking/x"},
    {"id": "z:lungeiv", "structure": "lunge/iv"},
    {"id": "z:lungev", "structure": "lunge/v"},
    {"id": "z:lungevi", "structure": "lunge/vi"},
    {"id": "z:lungevii", "structure": "lunge/vii"},
    {"id": "z:lungeviii", "structure": "lunge/viii"},
    {"id": "z:lungeix", "structure": "lunge/ix"},
    {"id": "z:lungex", "structure": "lunge/x"},
]


class EnchantmentStructureLoader(Plugin):
    api_version = "0.11"

    def on_load(self) -> None:
        """Called when the plugin is loaded"""
        self.logger.info("Loading Enchantment Structure Loader...")
        self.enchant_map = {item["id"]: item["structure"] for item in ENCHANTMENT_ITEMS}

    def on_enable(self) -> None:
        """Called when the plugin is enabled"""
        self.logger.info("Enchantment Structure Loader plugin enabled!")
        self.logger.info(f"Monitoring {len(self.enchant_map)} enchantment items")

        # Schedule repeating task to check inventories every second (20 ticks)
        self.server.scheduler.run_task(
            plugin=self,
            task=self.check_inventories,
            delay=0,
            period=20
        )

    def on_disable(self) -> None:
        """Called when the plugin is disabled"""
        self.logger.info("Enchantment Structure Loader plugin disabled!")

    def check_inventories(self) -> None:
        """Check all players' inventories for enchantment items"""
        try:
            for player in self.server.online_players:
                inventory = player.inventory
                if not inventory:
                    continue

                # Check all inventory slots
                for slot in range(inventory.size):
                    try:
                        item = inventory.get_item(slot)
                        if not item:
                            continue

                        # Get the string ID of the item type
                        item_type_id = str(item.type)

                        # Check if this item matches any enchantment item
                        if item_type_id in self.enchant_map:
                            structure_name = self.enchant_map[item_type_id]

                            self.logger.info(f"Found enchantment item '{item_type_id}' for player {player.name}, mapping to structure '{structure_name}'")

                            # Remove the item from inventory
                            inventory.set_item(slot, None)

                            # Load structure at player's location using server privileges
                            try:
                                # Get player's position and dimension for the command
                                location = player.location
                                x, y, z = int(location.x), int(location.y), int(location.z)
                                dimension = player.dimension

                                # Log player's current dimension and location
                                self.logger.info(f"Player {player.name} is in dimension '{dimension.name}' at ({x}, {y}, {z})")

                                # Map dimension names to proper Bedrock dimension IDs
                                dimension_name = dimension.name.lower()

                                # Handle different dimension name formats
                                # Bedrock uses simple dimension names without namespace in execute command
                                if dimension_name in ["overworld", "minecraft:overworld"]:
                                    # For overworld, use simple command without execute
                                    command = f'structure load "{structure_name}" {x} {y} {z}'
                                elif dimension_name in ["nether", "the_nether", "minecraft:the_nether", "thenether"]:
                                    command = f'execute in nether run structure load "{structure_name}" {x} {y} {z}'
                                elif dimension_name in ["end", "the_end", "minecraft:the_end", "theend"]:
                                    command = f'execute in the_end run structure load "{structure_name}" {x} {y} {z}'
                                else:
                                    # For custom dimensions, use the name without namespace
                                    # Remove minecraft: prefix if present
                                    if ":" in dimension.name:
                                        dim_id = dimension.name.split(":", 1)[1]
                                    else:
                                        dim_id = dimension.name
                                    command = f'execute in {dim_id} run structure load "{structure_name}" {x} {y} {z}'

                                self.logger.info(f"Executing command: {command}")

                                # Execute the command as the server
                                result = self.server.dispatch_command(self.server.command_sender, command)

                                if result:
                                    self.logger.info(
                                        f"Successfully loaded structure '{structure_name}' for player {player.name} at ({x}, {y}, {z}) in {dimension.name}"
                                    )
                                else:
                                    self.logger.error(
                                        f"Failed to execute structure load command for '{structure_name}' at ({x}, {y}, {z}) in {dimension.name}"
                                    )
                            except Exception as structure_error:
                                self.logger.error(f"Error loading structure '{structure_name}': {structure_error}")
                                # Re-add the item to inventory if structure loading failed
                                inventory.set_item(slot, item)
                    except Exception as e:
                        self.logger.error(f"Error checking slot {slot}: {e}")
                        continue
        except Exception as e:
            self.logger.error(f"Error in check_inventories: {e}")