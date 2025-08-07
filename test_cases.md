# Test Cases for WhatsApp Application

| Test Case ID | Description | Input | Expected Output | Test Type |
|-------------|-------------|-------|----------------|-----------|
| F001 | Verify text message sending | Send "Hello" to a contact | Message delivered with single tick, then double tick when delivered to recipient's device, blue tick when read | Functional |
| F002 | Verify media sharing - photo | Select and send a photo from gallery | Photo should be delivered and visible to recipient | Functional |
| F003 | Verify media sharing - video | Record and send a 10-second video | Video should be delivered and playable by recipient | Functional |
| F004 | Verify HD media quality option | Toggle HD quality option and send photo | Photo should be sent in selected quality (HD or compressed) | Functional |
| F005 | Verify status update | Upload a photo as status | Status should be visible to contacts for 24 hours | Functional |
| F006 | Verify status privacy settings | Change status privacy to "My Contacts except..." | Status should only be visible to selected contacts | Functional |
| F007 | Verify profile picture update | Change profile picture | New profile picture should be visible to contacts | Functional |
| F008 | Verify chat backup | Initiate manual backup | Chat history should be backed up to cloud storage | Functional |
| F009 | Verify chat restore | Reinstall app and restore from backup | All previous chats should be restored | Functional |
| F010 | Verify media download | Receive photo and download | Photo should be saved to device gallery | Functional |
| F011 | Verify group creation | Create new group with 3 contacts | Group should be created with selected contacts | Functional |
| F012 | Verify group admin functions | Assign admin privileges to a group member | Member should have admin capabilities | Functional |
| F013 | Verify UPI transaction | Send ₹10 to a contact via UPI | Money should be transferred and transaction receipt shown | Functional |
| F014 | Verify contact blocking | Block a contact | Blocked contact should not be able to message or call | Functional |
| F015 | Verify audio call | Initiate audio call to contact | Call should connect with clear audio | Functional |
| F016 | Verify video call | Initiate video call to contact | Call should connect with clear video and audio | Functional |
| F017 | Verify notification settings | Disable notifications for a specific chat | No notifications should appear for that chat | Functional |
| F018 | Verify message search | Search for keyword in chat history | All messages containing keyword should be displayed | Functional |
| F019 | Verify multi-device login | Login on secondary device | Chats should sync across both devices | Functional |
| F020 | Verify last seen privacy | Change last seen to "Nobody" | Contacts should not see user's last seen timestamp | Functional |
| F021 | Verify chat archiving | Archive a chat | Chat should move to archived section | Functional |
| F022 | Verify message reaction | React with thumbs up emoji to a message | Emoji reaction should appear on the message | Functional |
| F023 | Verify message forwarding | Forward a message to another contact | Message should be delivered with forwarded label | Functional |
| F024 | Verify starred messages | Star an important message | Message should appear in starred messages section | Functional |
| F025 | Verify QR code contact sharing | Generate and scan QR code | Contact should be added to recipient's contacts | Functional |
| NF001 | Verify message delivery time | Send message with slow network | Message should be delivered within 5 seconds | Non-functional (Performance) |
| NF002 | Verify app load time | Open the application | App should load within 3 seconds | Non-functional (Performance) |
| NF003 | Verify end-to-end encryption | Send message and check encryption status | Lock icon should be visible indicating encryption | Non-functional (Security) |
| NF004 | Verify app behavior under poor network | Use app with 2G network | App should adapt and still function with reduced quality | Non-functional (Reliability) |
| NF005 | Verify concurrent user support | Login during peak usage time | App shoul