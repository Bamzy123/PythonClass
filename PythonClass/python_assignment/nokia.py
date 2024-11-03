function = int(input("List of menu fnctions:\n 1. Phonebook \n 2. Messages \n 3. chat \n 4. Call register \n 5. Tones \n 6. Settings \n 7. Call divert \n 8. Games \n 9. Calculator \n 10. Reminders \n 11. Clock \n 12. Profiles \n 13. SIM services \n"))
match function:
	case 1:
		phonebook = int(input("Phonebook: \n 1. Search \n 2. Service Nos. \n 3. Add name \n 4. Erase \n 5. Edit \n 6. Assign tone \n 7. Send b' card \n 8. Option \n 9. Speed dials \n 10. Voice tags \n"))
		match phonebook:
				case 1:
					print("Search")
				case 2:
					print("Service Nos")
				case 3:
					print("Add name")
				case 4:
					print("Erase")
				case 5:
					print("Edit")
				case 6:
					print("Assign tone")
				case 7:
					print("Send b' card")
				case 8:
					option = int(input("Option: \n 1. Type of view \n 2. Memory status \n"))
					match option:
							case 1:
								print("Type of view")
							case 2:
								print("Memory status")
				case 9:
					print("Speed dials")
				case 10:
					print("Voice tags")
	case 2:
		message = int(input("Messages: \n 1. Write message \n 2. Inbox \n 3. Outbox \n 4. Picture messages \n 5. Templates \n 6. Smileys \n 7. Message settings \n 8. Info service \n 9. Voice mailbox number \n 10. Service command editor \n"))
		match message:
				case 1:
					print("Write message")
				case 2:
					print("Inbox")
				case 3:
					print("Outbox")
				case 4:
					print("Picture messages")
				case 5:
					print("Templates")
				case 6:
					print("Smileys")
				case 7:
					message_setting = int (input("message settings:\n 1. Set \n 2. Common \n"))
					match message_setting:
							case 1:
								set = int(input("Set: \n 1. Message centre number \n 2. Messages sent as \n 3. Message validity \n"))
								match set:
										case 1:
											print("Message centre number")
										case 2:
											print("Messages sent as")
										case 3:
											print("Message validity")
							case 2:
								common = int(input("Common: \n 1. Delivery reports \n 2. Reply via same centre \n 3. Charater support \n"))
								match common:
										case 1:
											print("Delivery reports")
										case 2:
											print("Reply via same centre")
										case 3:
											print("Charater support")
				case 8:
					print("Info service")
				case 9:
					print("Voice mailbox number")
				case 10:
					print("Service command editor")
	case 3:
		print("Chat")
	case 4:
		call_register = int(input("Call rigister: \n 1. Missed calls \n 2. Received calls \n 3. Dialled numbers \n 4. Erase recent call lists \n 5. Show call duration \n 6. Show call cost \n 7. Call cost settings \n 8. Prepaid credit \n"))
		match call_register:
				case 1:
					print("Missed calls")
				case 2:
					print("Received calls")
				case 3:
					print("Dialled numbers")
				case 4:
					print("Erase recent call lists")
				case 5:
					duration = int(input("Call duration: \n 1. Last call duration \n 2. All calls' duration \n 3. Received calls' duration \n 4. Dialled calls' duration \n 5. Clear timer \n"))
					match duration:
							case 1:
								print("Last call duration")
							case 2:
								print("All calls' duration")
							case 3:
								print("Received calls' duration")
							case 4:
								print("Dialled calls' duration")
							case 5:
								print("Clear timer")
				case 6:
					cost = int(input("Call cost: \n 1. Last call cost \n 2. All calls' cost \n 3. Clear counter \n"))
					match cost:
							case 1:
								print("Last call cost")
							case 2:
								print("All calls' cost")
							case 3:
								print("Clear counter")
				case 7:
					cost_setting = int(input("Call settings: \n 1. Call cost limit \n 2. Show costs in \n"))
					match cost_setting:
								case 1:
									print("Call cost limit")
								case 2:
									print("All calls' cost")
	case 5:
		tone = int(input("Tones: \n 1. Ringing tone \n 2. Ringing volume \n 3. Incoming call alert \n 4. Composer \n 5. Message alert tone \n 6. Keypad tones \n 7. Warning and game tones \n 8. Vibrating alert \n 9. Screen saver \n"))
		match tone:
				case 1:
					print("Ringing tone")
				case 2:
					print("Ringing volume")
				case 3:
					print("Incoming call alert")
				case 4:
					print("Composer")
				case 5:
					print("Message alert tone")
				case 6:
					print("Keypad tones")
				case 7:
					print("Warning and game tones")
				case 8:
					print("Vibrating alert")
				case 9:
					print("Screen saver")
	case 6:
		 setting = int(input("Settings: \n 1. Call settings \n 2. Phone settings \n 3. Security settings \n 4. Restore factory settings \n"))
		 match setting:
					case 1:
						call_setting = int(input("call settings: \n 1. Automatic redial \n 2. Speed dialling \n 3. Call waiting option \n 4. Own number sending \n 5. Phone line in use \n 6. Automatic answer \n"))
						match call_setting:
									case 1:
										print("Automatic redial")
									case 2:
										print("Speed dialling")
									case 3:
										print("Call waiting option")
									case 4:
										print("Own number sending")
									case 5:
										print("Phone line in use")
									case 6:
										print("Automatic answer")
					case 2:
						phone_setting = int(input("Phone settings: \n 1. Language \n 2. Cell info display \n 3. Welcome note \n 4. Network selection \n 5. Light \n 6. Confirm SIM service actions \n"))
						match phone_setting:
									case 1:
										print("Language")
									case 2:
										print("Cell info display")
									case 3:
										print("Welcome note")
									case 4:
										print("Network selection")
									case 5:
										print("Light")
									case 6:
										print("Confirm SIM service actions")
					case 3:
						security_setting = int(input("Security settings: \n 1. PIN code request \n 2. Call barring service \n 3. Fixed dialling \n 4. Closed user group \n 5. Phone security \n 6. Change access codes \n"))
						match security_setting:
									case 1:
										print("PIN code request")
									case 2:
										print("Call barring service")
									case 3:
										print("Fixed dialling")
									case 4:
										print("Closed user group")
									case 5:
										print("Phone security")
									case 6:
										print("Change access codes")
					case 4:
						print("Restore factory settings")
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminder")
	case 11:
		clock = int(input("Clock: \n 1. Alarm clock \n 2. Clock settings \n 3. Data setting \n 4. Stopwatch \n 5. Countdown timer \n 6. Auto update of date and time \n"))
		match clock:
				case 1:
					print("Alarm clock")
				case 2:
					print("Clock settings")
				case 3:
					print("Data setting")
				case 4:
					print("Stopwatch")
				case 5:
					print("Countdown timer")
				case 6:
					print("Auto update of date and time")
	case 12:
		print("Profiles")
	case 13:
		print("SIM services")