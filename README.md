# Home Assistant homee integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Community Forum][forum-shield]][forum]

_Component to integrate with [homee][homee]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Integrate homee devices that binary state information like `on`/`off` or `open`/`close`.
`climate` | Integrate homee devices that provide temperature and can set a target temperature.
`light` | Integrate lights from homee.
`switch` | Integrate homee devices that can be switched `on`/`off` with optional power monitoring.

![homee][homee_logo]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `homee`.
4. Download _all_ the files from the `custom_components/homee/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant

## Configuration

The integration will attempt to discover homee cubes in your network. Discovery is experimental and has not been properly tested yet. I recommend to add your homee cube(s) manually:

1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "homee"
2. Select the "homee" integration from the list. If it does not show up you should check if it is installed correctly. Go to "Configuration" -> "Logs" and make sure there are no errors. Also make sure to restart home assistant after installation.
3. In the dialog enter the host (ip address of the homee cube) as well as the username and password of a homee account that can access your cube.
4. Hit submit. All supported devices will be automatically added to home assistant.

## Additional configuration

TODO: Customize device classes

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[homee]: https://hom.ee
[buymecoffee]: https://www.buymeacoffee.com/FreshlyBrewed
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/FreshlyBrewedCode/hacs-homee.svg?style=for-the-badge
[commits]: https://github.com/FreshlyBrewedCode/hacs-homee/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[homee_logo]: https://raw.githubusercontent.com/FreshlyBrewedCode/brands/master/custom_integrations/homee/logo.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/blueprint.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-FreshlyBrewedCode-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/FreshlyBrewedCode/hacs-homee.svg?style=for-the-badge
[releases]: https://github.com/FreshlyBrewedCode/hacs-homee/releases
