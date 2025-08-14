# Test Cases for WhatsApp Application

| Test Case ID | Description | Input | Expected Output | Test Type |
|--------------|-------------|-------|-----------------|-----------|
| F001 | Verify text message sending | Send "Hello" to a contact | Message delivered with single tick, then double tick when delivered to recipient's device, blue tick when read | Functional |
| F002 | Verify media sharing - photo | Select and send a photo from gallery | Photo should be delivered and visible to recipient with proper compression | Functional |
| F003 | Verify media sharing - video | Record and send a video | Video should be delivered and playable by recipient | Functional |
| F004 | Verify HD media sharing | Enable HD quality and send a photo | Photo should be delivered in HD quality | Functional |
| F005 | Verify status upload | Upload a photo as status | Status should be visible to contacts for 24 hours | Functional |
| F006 | Verify status privacy | Set status privacy to "My Contacts except..." | Status should be visible only to selected contacts | Functional |
| F007 | Verify profile picture update | Change profile picture | New profile picture should be visible to contacts | Functional |
| F008 | Verify chat backup | Initiate manual backup | Chat history should be backed up to cloud storage | Functional |
| F009 | Verify chat restore | Reinstall app and restore from backup | All previous chats should be restored | Functional |
| F010 | Verify media download | Receive a photo and download it | Photo should be saved to device gallery | Functional |
| F011 | Verify group creation | Create a new group and add 5 contacts | Group should be created with all added members | Functional |
| F012 | Verify UPI transaction | Send ₹100 to a contact via UPI | Money should be transferred and transaction record created | Functional |
| F013 | Verify contact blocking | Block a contact | Messages, calls, and status updates from blocked contact should not be received | Functional |
| F014 | Verify audio call | Initiate audio call to a contact | Call should connect with clear audio | Functional |
| F015 | Verify video call | Initiate video call to a contact | Call should connect with clear video and audio | Functional |
| F016 | Verify notification settings | Disable notifications for a specific group | No notifications should appear for messages in that group | Functional |
| F017 | Verify message search | Search for a specific text in chat history | All messages containing the search term should be displayed | Functional |
| F018 | Verify multi-device login | Login to WhatsApp Web while using mobile app | Both devices should show synchronized messages | Functional |
| F019 | Verify last seen privacy | Set last seen to "Nobody" | No contacts should be able to see user's last seen timestamp | Functional |
| F020 | Verify chat archiving | Archive a chat | Chat should move to archived section | Functional |
| F021 | Verify message reaction | React with 👍 to a message | Reaction should be visible to all chat participants | Functional |
| F022 | Verify message forwarding | Forward a message to another contact | Message should be delivered with "Forwarded" label | Functional |
| F023 | Verify starred messages | Star an important message | Message should appear in starred messages section | Functional |
| F024 | Verify QR code contact sharing | Generate and scan QR code | Contact should be added to recipient's contact list | Functional |
| F025 | Verify chat deletion | Delete a chat | Chat should be permanently removed | Functional |
| NF001 | Verify message delivery time | Send message with slow network | Message should be delivered within acceptable time frame (< 5 seconds) | Non-functional |
| NF002 | Verify app performance under load | Open app with 1000+ messages | App should load within 3 seconds | Non-functional |
| NF003 | Verify end-to-end encryption | Send sensitive information | Message should be encrypted and secure | Non-functional |
| NF004 | Verify UI consistency | Check UI elements across different screens | UI should be consistent and follow design guidelines | Non-functional |
| NF005 | Verify app reliability | Use app continuously for 24