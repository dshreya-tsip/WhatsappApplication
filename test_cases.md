# Test Cases for WhatsApp Application

| Test Case ID | Description | Input | Expected Output | Test Type |
|--------------|-------------|-------|-----------------|-----------|
| F001 | Verify text message sending | Send "Hello" to a contact | Message delivered with single tick, then double tick when delivered to recipient's device, blue tick when read | Functional |
| F002 | Verify media sharing - photo | Select and send a photo from gallery | Photo should be delivered and displayed correctly on recipient's device | Functional |
| F003 | Verify media sharing - video | Record and send a video | Video should be delivered and playable on recipient's device | Functional |
| F004 | Verify status upload | Upload a photo as status | Status should be visible to contacts for 24 hours | Functional |
| F005 | Verify profile picture update | Change profile picture | New profile picture should be visible to contacts based on privacy settings | Functional |
| F006 | Verify chat backup | Initiate chat backup | All chats and media should be backed up to cloud storage | Functional |
| F007 | Verify chat restore | Restore from backup | All backed up chats and media should be restored | Functional |
| F008 | Verify media download | Download received image | Image should be saved to device gallery | Functional |
| F009 | Verify group creation | Create a new group with 3 contacts | Group should be created with all members added | Functional |
| F010 | Verify UPI transaction | Send ₹100 to a contact | Money should be transferred successfully with confirmation | Functional |
| F011 | Verify contact blocking | Block a contact | No messages or calls should be received from blocked contact | Functional |
| F012 | Verify audio call | Initiate audio call to contact | Call should connect with clear audio | Functional |
| F013 | Verify video call | Initiate video call to contact | Call should connect with clear audio and video | Functional |
| F014 | Verify notification settings | Disable notifications for a specific chat | No notifications should appear for messages from that chat | Functional |
| F015 | Verify message search | Search for keyword in chat history | All messages containing the keyword should be displayed | Functional |
| F016 | Verify multi-device login | Login on second device | Chats should sync across both devices | Functional |
| F017 | Verify privacy settings | Change "Last Seen" to "Nobody" | Last seen status should not be visible to any contacts | Functional |
| F018 | Verify chat archiving | Archive a chat | Chat should move to archived section | Functional |
| F019 | Verify message reactions | React with 👍 to a message | Reaction should be visible to all chat participants | Functional |
| F020 | Verify message forwarding | Forward a message to another contact | Message should be delivered with "Forwarded" label | Functional |
| NF001 | Verify message delivery time | Send message with slow network | Message should be delivered within 5 seconds | Non-functional |
| NF002 | Verify app performance with multiple chats | Open app with 100+ active chats | App should load within 3 seconds | Non-functional |
| NF003 | Verify end-to-end encryption | Send confidential message | Message should be encrypted and only readable by sender and recipient | Non-functional |
| NF004 | Verify UI consistency | Check UI elements across different screens | UI should be consistent in design and behavior | Non-functional |
| NF005 | Verify app availability | Use app continuously for 24 hours | No crashes or service interruptions | Non-functional |
| NF006 | Verify cross-platform compatibility | Send message from Android to iOS | Message should appear identical on both platforms | Non-functional |
| NF007 | Verify bandwidth usage | Send 10 messages | Data usage should not exceed 50KB | Non-functional |
| NF008 | Verify battery consumption | Use app for 1 hour | Battery usage should not exceed 5% | Non-functional |
| NF009 | Verify app response time | Tap on chat | Chat should open within 1 second | Non-functional |
| NF010 | Verify load testing | Simulate 1000 concurrent