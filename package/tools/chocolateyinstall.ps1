
$ErrorActionPreference = 'Stop'; 
$packageName = 'package'
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$fileLocation = Join-Path $toolsDir 'PSLab-Desktop-Setup-2.5.2.exe'


$packageArgs = @{
  packageName   = $packageName
  softwareName  = 'package*'
  file          = $fileLocation
  fileType      = 'EXE'
   silentArgs   = '/S' 
   validExitCodes= @(0)
  checksum      = ''
  checksumType  = 'sha256' 
            
 
   
}

Install-ChocolateyPackage @packageArgs 


